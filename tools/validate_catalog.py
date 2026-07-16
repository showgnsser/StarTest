#!/usr/bin/env python3
"""校验 StarTest 固定案例、说明、运行元数据和图片链接。"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = ROOT / "StarTrack"
SIGNALS = {"GPS_L1CA", "BDS_B1I", "GPS_L5"}
SCENARIOS = {
    "01_pull_in_sensitivity",
    "02_sustained_unaided",
    "03_sustained_aided",
    "04_doppler_dynamics",
    "05_step_transitions",
    "06_slow_fade_recovery",
    "07_threshold_hysteresis",
    "08_endurance",
}
README_SECTIONS = (
    "## 现实场景",
    "## 输入",
    "## 真值",
    "## 预期结果",
    "## 实际结果",
    "## 结论",
)
RUN_PATTERN = re.compile(r"startrack-[0-9a-f]{7,40}_[A-Za-z0-9._-]+$")
DATE_PATTERN = re.compile(r"(?:19|20)\d{2}[-_]\d{2}[-_]\d{2}")


def load_json(path):
    """读取一个UTF-8 JSON文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def check(condition, message, errors):
    """把错误加入列表，允许一次显示全部结构问题。"""
    if not condition:
        errors.append(message)


def validate_run(run, scenario, readme, errors):
    """校验一个已发布版本运行目录。"""
    check(RUN_PATTERN.fullmatch(run.name) is not None,
          "invalid run directory: {}".format(run), errors)
    summary_path = run / "summary.json"
    metrics_path = run / "metrics.csv"
    figures = run / "figures"
    check(summary_path.is_file(), "missing {}".format(summary_path), errors)
    check(metrics_path.is_file(), "missing {}".format(metrics_path), errors)
    check(figures.is_dir(), "missing {}".format(figures), errors)
    if not summary_path.is_file():
        return

    summary = load_json(summary_path)
    for field in ("git_sha", "profile_version", "run_timestamp",
                  "case_id", "seeds"):
        check(field in summary,
              "{} missing {}".format(summary_path, field), errors)
    check(summary.get("case_id") == scenario.get("case_id"),
          "{} case_id mismatch".format(summary_path), errors)
    expected_seeds = summary.get("seeds", [])
    for seed in expected_seeds:
        seed_root = run / "seed-{:03d}".format(int(seed))
        check((seed_root / "observations.csv").is_file(),
              "missing seed observations: {}".format(seed_root), errors)
        check((seed_root / "state_events.csv").is_file(),
              "missing seed events: {}".format(seed_root), errors)

    if metrics_path.is_file():
        with metrics_path.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream))
        check(bool(rows), "empty metrics file: {}".format(metrics_path), errors)
        required = {"seed", "status", "doppler_rms_hz",
                    "doppler_p95_hz", "code_phase_p95_chips"}
        if rows:
            check(required.issubset(rows[0]),
                  "metrics units/fields incomplete: {}".format(metrics_path),
                  errors)

    pngs = list(figures.glob("*.png")) if figures.is_dir() else []
    check(bool(pngs), "run has no PNG figures: {}".format(run), errors)
    if pngs:
        relative_prefix = "runs/{}/figures/".format(run.name)
        check(relative_prefix in readme,
              "scenario README does not link figures for {}".format(run.name),
              errors)


def validate():
    """校验全部信号和固定案例。"""
    errors = []
    check(CATALOG_ROOT.is_dir(), "missing StarTrack catalog root", errors)
    actual_signals = {path.name for path in CATALOG_ROOT.iterdir()
                      if path.is_dir()} if CATALOG_ROOT.is_dir() else set()
    check(actual_signals == SIGNALS,
          "signals mismatch: {}".format(sorted(actual_signals)), errors)

    case_ids = set()
    for signal in sorted(SIGNALS):
        signal_root = CATALOG_ROOT / signal
        check((signal_root / "README.md").is_file(),
              "missing signal README: {}".format(signal), errors)
        actual_scenarios = {path.name for path in signal_root.iterdir()
                            if path.is_dir()} if signal_root.is_dir() else set()
        check(actual_scenarios == SCENARIOS,
              "{} scenarios mismatch: {}".format(
                  signal, sorted(actual_scenarios)), errors)
        for folder in sorted(SCENARIOS):
            root = signal_root / folder
            readme_path = root / "README.md"
            scenario_path = root / "scenario.json"
            check(readme_path.is_file(), "missing {}".format(readme_path), errors)
            check(scenario_path.is_file(), "missing {}".format(scenario_path),
                  errors)
            if not readme_path.is_file() or not scenario_path.is_file():
                continue
            readme = readme_path.read_text(encoding="utf-8")
            for section in README_SECTIONS:
                check(section in readme,
                      "{} missing section {}".format(readme_path, section),
                      errors)
            scenario = load_json(scenario_path)
            case_id = str(scenario.get("case_id", ""))
            check(case_id and case_id not in case_ids,
                  "duplicate or empty case_id: {}".format(case_id), errors)
            case_ids.add(case_id)
            check(DATE_PATTERN.search(case_id) is None,
                  "date found in stable case_id: {}".format(case_id), errors)
            check(scenario.get("signal") == signal,
                  "signal mismatch in {}".format(scenario_path), errors)
            check(scenario.get("test_set") == "Qualification",
                  "test_set mismatch in {}".format(scenario_path), errors)
            check(float(scenario.get("duration_s", 0.0)) > 0.0,
                  "duration_s invalid in {}".format(scenario_path), errors)
            check(bool(scenario.get("seeds")),
                  "seeds missing in {}".format(scenario_path), errors)
            test_input = scenario.get("input", {})
            check(test_input.get("stream_format") == "binary 3-bit I/Q",
                  "stream format missing in {}".format(scenario_path), errors)
            check(bool(test_input.get("acquisition_frequency_errors_hz")),
                  "frequency error matrix missing in {}".format(
                      scenario_path), errors)
            check(bool(test_input.get("acquisition_code_errors_chips")),
                  "code error matrix missing in {}".format(scenario_path),
                  errors)
            clock = scenario.get("clock_profile", {})
            check(clock.get("id") == "GOOD_TCXO_V1",
                  "clock profile mismatch in {}".format(scenario_path), errors)
            acceptance = scenario.get("acceptance", {})
            for field in ("min_carrier_valid_ratio", "max_doppler_rms_hz",
                          "max_doppler_p95_hz",
                          "max_code_phase_p95_chips"):
                check(field in acceptance,
                      "{} missing acceptance unit {}".format(
                          scenario_path, field), errors)

            runs = root / "runs"
            check(runs.is_dir(), "missing runs directory: {}".format(runs),
                  errors)
            if runs.is_dir():
                for run in runs.iterdir():
                    if run.name.startswith(".") or not run.is_dir():
                        continue
                    validate_run(run, scenario, readme, errors)
    return errors, len(case_ids)


def main():
    """输出校验统计并设置进程退出码。"""
    try:
        errors, count = validate()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print("[fatal] {}".format(error), file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print("[error] {}".format(error), file=sys.stderr)
        print("Validation failed with {} errors".format(len(errors)),
              file=sys.stderr)
        return 1
    print("Validated {} fixed Qualification scenarios".format(count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
