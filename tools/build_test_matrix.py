#!/usr/bin/env python3
"""从公开黑盒结果生成 GitHub 可浏览的逐用例测试矩阵。"""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = ROOT / "results" / "StarTrack"
OUTPUT = ROOT / "TEST_MATRIX.md"


def load_json(path: Path) -> dict:
    """读取可选 JSON；历史结果缺少文件时返回空字典。"""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def first_number(text: str, labels: list[str]) -> str:
    """从公开结果说明中提取一个数值字段。"""
    for label in labels:
        match = re.search(
            r"(?:-\s*)?" + label + r"(?:[：:]|为)\s*`?([-+0-9.]+)", text)
        if match:
            return match.group(1)
    return ""


def cn0_text(scenario: dict, markdown: str) -> str:
    """把 C/N0 时间表压缩成适合表格显示的轨迹。"""
    points = scenario.get("cn0_schedule") or scenario.get("cn0_points") or []
    values = []
    for point in points:
        if isinstance(point, dict):
            value = point.get("cn0_db_hz")
        elif isinstance(point, (list, tuple)) and len(point) >= 2:
            value = point[1]
        else:
            value = None
        if value is None:
            continue
        value_text = f"{float(value):g}"
        if not values or values[-1] != value_text:
            values.append(value_text)
    if values:
        return " -> ".join(values)

    scalar = scenario.get("cn0_db_hz")
    if scalar is not None:
        return f"{float(scalar):g}"

    match = re.search(r"C/N0[^：:]*[：:]\s*(.+)", markdown)
    if match:
        return match.group(1).strip().strip("`")
    return "-"


def result_status(result: dict, markdown: str) -> str:
    """兼容新旧公开结果格式，返回通过、失败或记录。"""
    status = str(result.get("status", "")).upper()
    if (status == "PASS" or result.get("tracking_passed") is True or
            result.get("passed") is True):
        return "通过"
    if (status == "FAIL" or result.get("tracking_passed") is False or
            result.get("passed") is False):
        return "失败"
    if "Overall: **PASS**" in markdown:
        return "通过"
    if "Overall: **FAIL**" in markdown:
        return "失败"
    if "跟踪判定：通过" in markdown or "跟踪判定：`PASS`" in markdown:
        return "通过"
    if "跟踪判定：失败" in markdown or "跟踪判定：`FAIL`" in markdown:
        return "失败"

    conclusion = re.search(r"## 结论\s+([^#]+)", markdown)
    if conclusion:
        text = conclusion.group(1)
        if "失败" in text or "未通过" in text:
            return "失败"
        if "通过" in text:
            return "通过"
    return "记录"


def key_metrics(result: dict, markdown: str) -> str:
    """提取最常用的频差和码差指标，不暴露算法内部量。"""
    tail = result.get("tail", {})
    freq = tail.get("doppler_rms_hz", result.get("tail_doppler_rms_hz"))
    code = tail.get("code_p95_chips", result.get("tail_code_p95_chips"))
    if freq is None:
        freq_text = first_number(
            markdown, ["频差 RMS", "频差RMS", "多普勒 RMS"])
        freq = float(freq_text) if freq_text else None
    if code is None:
        code_text = first_number(
            markdown, ["码相位误差 P95", "码差 P95", "码差P95"])
        code = float(code_text) if code_text else None

    fields = []
    if freq is not None:
        fields.append(f"频差RMS {float(freq):.4f} Hz")
    if code is not None:
        fields.append(f"码差P95 {float(code):.4f} chip")
    return "；".join(fields) if fields else "见详情"


def table_escape(value: object) -> str:
    """转义 Markdown 表格中的分隔符和换行。"""
    return str(value).replace("|", "\\|").replace("\n", " ")


def collect_cases() -> list[dict]:
    """收集所有包含 result.md 的正式公开测试用例。"""
    cases = []
    for result_md in RESULT_ROOT.rglob("result.md"):
        relative = result_md.relative_to(RESULT_ROOT)
        parts = relative.parts
        if len(parts) < 5:
            continue
        signal, campaign, run_date, case_name = parts[:4]
        markdown = result_md.read_text(encoding="utf-8")
        scenario = load_json(result_md.with_name("scenario.json"))
        result = load_json(result_md.with_name("result.json"))

        duration = scenario.get("duration_s", result.get("duration_s"))
        if duration is None:
            duration_text = first_number(markdown, ["时长"])
            duration = float(duration_text) if duration_text else None
        seed = scenario.get("seed", result.get("seed", "-"))
        initial_state = scenario.get("initial_state", "-")

        cases.append({
            "signal": signal,
            "campaign": campaign,
            "date": run_date,
            "case": case_name,
            "duration": f"{float(duration):g} s" if duration is not None else "-",
            "seed": seed,
            "cn0": cn0_text(scenario, markdown),
            "state": initial_state,
            "status": result_status(result, markdown),
            "metrics": key_metrics(result, markdown),
            "link": result_md.relative_to(ROOT).as_posix(),
        })
    return sorted(cases, key=lambda item: (
        item["signal"], item["campaign"], item["date"], item["case"]))


def render(cases: list[dict]) -> str:
    """生成总览和按信号分组的逐用例链接表。"""
    status_counts = Counter(case["status"] for case in cases)
    signal_counts = Counter(case["signal"] for case in cases)
    lines = [
        "# StarTrack 测试用例矩阵",
        "",
        f"> 更新日期：{date.today().isoformat()}。本页由 `tools/build_test_matrix.py` 从公开结果自动生成。",
        "",
        "该矩阵只汇总测试场景、外部输入、公开输出和验收结论。算法原理与内部参数请查阅 StarTrack 仓库。",
        "",
        "## 总览",
        "",
        "| 信号 | 用例数 |",
        "|---|---:|",
    ]
    for signal in sorted(signal_counts):
        lines.append(f"| {table_escape(signal)} | {signal_counts[signal]} |")
    lines.extend([
        "",
        f"共 {len(cases)} 个用例：通过 {status_counts['通过']}，失败 {status_counts['失败']}，仅记录 {status_counts['记录']}。",
        "",
        "失败用例不会删除，它们是边界和回归测试的重要基线。",
    ])

    for signal in sorted(signal_counts):
        lines.extend([
            "",
            f"## {signal}",
            "",
            "| 日期 | 测试集 | 用例 | 时长 | 种子 | C/N0 dB-Hz | 初始状态 | 结果 | 关键输出 | 详情 |",
            "|---|---|---|---:|---:|---|---|---|---|---|",
        ])
        for case in (item for item in cases if item["signal"] == signal):
            link = f"[查看]({case['link']})"
            values = [
                case["date"], case["campaign"], case["case"], case["duration"],
                case["seed"], case["cn0"], case["state"], case["status"],
                case["metrics"], link,
            ]
            lines.append("| " + " | ".join(table_escape(value) for value in values) + " |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """重建测试矩阵。"""
    cases = collect_cases()
    OUTPUT.write_text(render(cases), encoding="utf-8", newline="\n")
    print(f"Generated {OUTPUT} with {len(cases)} cases")


if __name__ == "__main__":
    main()
