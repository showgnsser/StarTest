#!/usr/bin/env python3
"""将已完成的三信号牵引 Qualification 结果发布到固定目录。"""

from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT.parent / "StarTrack" / "WorkSpace" / "FixedSuite"
GIT_SHA = "503cdeae75a8a9cd15acbc876eac5334be7d892e"
PROFILE_VERSION = "pullin-v2"
RUN_NAME = "startrack-{}_{}".format(GIT_SHA[:7], PROFILE_VERSION)

SIGNALS = {
    "GPS_L1CA": {
        "campaign": "qualification_pullin_final",
        "target_db_hz": 22.0,
        "representative": "pullin_22db_fp62p5_cp0p30_s20260716",
    },
    "BDS_B1I": {
        "campaign": "b1i_qualification_pullin",
        "target_db_hz": 24.0,
        "representative": "pullin_24db_fp62p5_cp0p3_s20260716",
    },
    "GPS_L5": {
        "campaign": "l5_qualification_boundary",
        "target_db_hz": 28.0,
        "representative": "pullin_28db_fp31p25_cp0p3_s20260716",
    },
}


def read_csv(path):
    """读取UTF-8 CSV并返回字典列表。"""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows, fieldnames):
    """以稳定字段顺序写出UTF-8 CSV。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames,
                                extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def source_output(campaign_root, run_name, suffix):
    """定位一个源运行的公开CSV输出。"""
    output_root = campaign_root / "results" / run_name
    matches = list(output_root.glob("*{}".format(suffix)))
    if len(matches) != 1:
        raise RuntimeError("expected one {} in {}".format(suffix, output_root))
    return matches[0]


def aggregate_seed_csv(campaign_root, rows, seed, suffix, output):
    """把同一随机种子的多个牵引误差组合合并到一份公开CSV。"""
    combined = []
    fields = []
    for row in rows:
        if int(row["seed"]) != seed:
            continue
        run_name = "{}_s{}".format(row["scenario"], seed)
        source = source_output(campaign_root, run_name, suffix)
        source_rows = read_csv(source)
        if source_rows and not fields:
            fields = ["scenario"] + list(source_rows[0].keys())
        for item in source_rows:
            combined.append(dict({"scenario": row["scenario"]}, **item))
    if not combined:
        raise RuntimeError("no {} rows for seed {}".format(suffix, seed))
    write_csv(output, combined, fields)


def metric_rows(rows):
    """提取固定公开指标，不发布内部算法参数。"""
    output = []
    for row in rows:
        output.append({
            "seed": row["seed"],
            "scenario": row["scenario"],
            "status": "PASS" if row["passed"].lower() == "true" else "FAIL",
            "pullin_time_s": row["pullin_time_s"],
            "doppler_rms_hz": row["doppler_rms_hz"],
            "doppler_p95_hz": row["doppler_p95_hz"],
            "code_phase_p95_chips": row["code_p95_chips"],
            "carrier_valid_ratio": row["cn0_valid_ratio"],
            "cn0_bias_db": row["cn0_bias_db"],
            "cn0_rmse_db": row["cn0_rmse_db"],
        })
    return output


def worst(rows, key):
    """返回一列有限数值中的最大值。"""
    values = []
    for row in rows:
        try:
            value = float(row[key])
        except (KeyError, TypeError, ValueError):
            continue
        if math.isfinite(value):
            values.append(value)
    return max(values) if values else None


def plot_matrix(rows, output, title):
    """绘制全部误差组合与种子的牵引指标。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    cases = sorted({row["scenario"] for row in rows})
    short = [case.replace("pullin_", "") for case in cases]
    positions = {case: index for index, case in enumerate(cases)}
    figure, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    fields = (
        ("pullin_time_s", "Pull-in time (s)", 20.0),
        ("doppler_rms_hz", "Tail Doppler RMS (Hz)", 5.0),
        ("code_p95_chips", "Tail code phase P95 (chip)", 0.2),
    )
    for axis, (field, label, limit) in zip(axes, fields):
        for row in rows:
            value = row.get(field, "")
            if value == "":
                continue
            axis.scatter(positions[row["scenario"]], float(value), s=24,
                         alpha=0.8)
        axis.axhline(limit, color="tab:red", linestyle="--", linewidth=1.0,
                     label="Acceptance limit")
        axis.set_ylabel(label)
        axis.grid(True, alpha=0.3)
        axis.legend(loc="upper right")
    axes[-1].set_xticks(range(len(cases)))
    axes[-1].set_xticklabels(short, rotation=25, ha="right")
    figure.suptitle(title)
    figure.tight_layout()
    figure.savefig(str(output), dpi=150)
    plt.close(figure)


def plot_trace(campaign_root, run_name, output, title):
    """绘制一个边界种子的时间序列，便于检查收敛过程。"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rows = read_csv(source_output(campaign_root, run_name, ".status.csv"))
    time_s = [float(row["time_s"]) for row in rows]
    doppler = [float(row["doppler_error_hz"]) for row in rows]
    code = [float(row["code_phase_error_chips"]) for row in rows]
    cn0 = [float(row["cn0_db_hz"]) if row["cn0_valid"] == "1" else math.nan
           for row in rows]

    figure, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    axes[0].plot(time_s, doppler, color="tab:red", linewidth=1.1)
    axes[0].axhspan(-5.0, 5.0, color="tab:red", alpha=0.08)
    axes[0].set_ylabel("Doppler error (Hz)")
    axes[1].plot(time_s, code, color="tab:green", linewidth=1.1)
    axes[1].axhspan(-0.2, 0.2, color="tab:green", alpha=0.08)
    axes[1].set_ylabel("Code error (chip)")
    axes[2].plot(time_s, cn0, color="tab:blue", linewidth=1.1)
    axes[2].set_ylabel("Estimated C/N0 (dB-Hz)")
    axes[2].set_xlabel("Tracking time (s)")
    for axis in axes:
        axis.grid(True, alpha=0.3)
    figure.suptitle(title)
    figure.tight_layout()
    figure.savefig(str(output), dpi=150)
    plt.close(figure)


def publish_signal(source_root, signal_id, config):
    """发布一个信号的五种子牵引结果。"""
    campaign_root = source_root / config["campaign"]
    matrix_path = campaign_root / "matrix_summary.csv"
    rows = [row for row in read_csv(matrix_path)
            if row.get("required", "").lower() == "true"]
    if not rows or not all(row["passed"].lower() == "true" for row in rows):
        raise RuntimeError("required pull-in matrix is incomplete: {}".format(
            matrix_path))

    scenario_root = ROOT / "StarTrack" / signal_id / "01_pull_in_sensitivity"
    scenario = json.loads((scenario_root / "scenario.json").read_text(
        encoding="utf-8"))
    run_root = scenario_root / "runs" / RUN_NAME
    if run_root.exists():
        raise RuntimeError("published run already exists: {}".format(run_root))
    run_root.mkdir(parents=True)

    seeds = sorted({int(row["seed"]) for row in rows})
    metrics = metric_rows(rows)
    write_csv(run_root / "metrics.csv", metrics, list(metrics[0].keys()))
    for seed in seeds:
        seed_root = run_root / "seed-{:03d}".format(seed)
        aggregate_seed_csv(campaign_root, rows, seed, ".status.csv",
                           seed_root / "observations.csv")
        aggregate_seed_csv(campaign_root, rows, seed, ".state.csv",
                           seed_root / "state_events.csv")

    figures = run_root / "figures"
    figures.mkdir()
    plot_matrix(rows, figures / "pullin_matrix.png",
                "{} pull-in qualification matrix".format(signal_id))
    plot_trace(campaign_root, config["representative"],
               figures / "representative_trace.png",
               "{} boundary pull-in, seed 20260716".format(signal_id))

    summary = {
        "schema_version": 1,
        "git_sha": GIT_SHA,
        "profile_version": PROFILE_VERSION,
        "run_timestamp": datetime.fromtimestamp(
            matrix_path.stat().st_mtime).astimezone().isoformat(),
        "case_id": scenario["case_id"],
        "seeds": seeds,
        "source_campaign": config["campaign"],
        "target_cn0_db_hz": config["target_db_hz"],
        "required_combinations": len(rows),
        "passed_combinations": sum(item["status"] == "PASS" for item in metrics),
        "status": "PASS",
        "worst_pullin_time_s": worst(rows, "pullin_time_s"),
        "worst_doppler_rms_hz": worst(rows, "doppler_rms_hz"),
        "worst_doppler_p95_hz": worst(rows, "doppler_p95_hz"),
        "worst_code_phase_p95_chips": worst(rows, "code_p95_chips"),
        "note": "Results predate the target-only catalog change; commit 503cdea freezes the tested implementation.",
    }
    (run_root / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n")
    print("published {}: {}/{} combinations".format(
        signal_id, summary["passed_combinations"], len(rows)))


def main():
    """解析源目录并发布三个信号。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args()
    for signal_id, config in SIGNALS.items():
        publish_signal(args.source_root, signal_id, config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
