#!/usr/bin/env python3
"""从固定案例和版本运行生成不含日期目录的 Qualification 矩阵。"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = ROOT / "StarTrack"
OUTPUT = ROOT / "TEST_MATRIX.md"


def load_json(path):
    """读取可选JSON，文件缺失时返回空字典。"""
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def latest_run(runs_root):
    """按summary中的运行时刻选择最新的版本运行。"""
    candidates = []
    if not runs_root.is_dir():
        return None, {}
    for run in runs_root.iterdir():
        if not run.is_dir():
            continue
        summary = load_json(run / "summary.json")
        candidates.append((str(summary.get("run_timestamp", "")), run,
                           summary))
    if not candidates:
        return None, {}
    _, run, summary = max(candidates, key=lambda item: (item[0], item[1].name))
    return run, summary


def status_text(summary):
    """返回公开运行的中文结论。"""
    status = str(summary.get("status", "")).upper()
    if status == "PASS":
        return "通过"
    if status == "FAIL":
        return "失败"
    return "待运行"


def target_text(scenario):
    """压缩显示一个案例的三个目标灵敏度。"""
    values = scenario.get("sensitivity_targets_db_hz", {})
    return "{}/{}/{}".format(
        values.get("pull_in", "-"),
        values.get("sustained_unaided", "-"),
        values.get("sustained_aided", "-"))


def render():
    """渲染固定案例总览。"""
    lines = [
        "# StarTrack 固定 Qualification 测试矩阵",
        "",
        "本页由 `tools/build_test_matrix.py` 从固定场景和版本运行生成。",
        "日期不是案例 ID 或目录的一部分；最新结果按 `summary.json` 的运行元数据选择。",
        "",
        "目标列依次为牵引、无辅助持续、已知位辅助持续 C/N0，单位 dB-Hz。",
    ]
    for signal_root in sorted(path for path in CATALOG_ROOT.iterdir()
                              if path.is_dir()):
        lines.extend([
            "",
            "## {}".format(signal_root.name),
            "",
            "| 固定案例 | 正式时长 | 最新/计划种子 | 三项目标 | 最新版本 | 运行类型 | 结果 | 详情 |",
            "|---|---:|---:|---|---|---|---|---|",
        ])
        for case_root in sorted(path for path in signal_root.iterdir()
                                if path.is_dir()):
            scenario = load_json(case_root / "scenario.json")
            run, summary = latest_run(case_root / "runs")
            run_name = run.name if run is not None else "-"
            link = (case_root / "README.md").relative_to(ROOT).as_posix()
            latest_seed_count = len(summary.get("seeds", []))
            planned_seed_count = len(scenario.get("seeds", []))
            seed_text = "{}/{}".format(latest_seed_count,
                                         planned_seed_count)
            run_type = summary.get("test_set", "-")
            lines.append(
                "| `{}` | {:g} s | {} | {} | `{}` | {} | {} | [查看]({}) |".
                format(
                    scenario.get("case_id", case_root.name),
                    float(scenario.get("duration_s", 0.0)),
                    seed_text, target_text(scenario), run_name, run_type,
                    status_text(summary), link))
    lines.append("")
    return "\n".join(lines)


def main():
    """重建固定测试矩阵。"""
    OUTPUT.write_text(render(), encoding="utf-8", newline="\n")
    print("Generated {}".format(OUTPUT))


if __name__ == "__main__":
    main()
