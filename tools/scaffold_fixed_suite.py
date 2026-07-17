#!/usr/bin/env python3
"""生成 StarTest 固定 Qualification 场景目录和说明文件。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STARTRACK_ROOT = ROOT / "StarTrack"
SEEDS_3 = [20260716, 20260717, 20260718]
SEEDS_5 = [20260716, 20260717, 20260718, 20260719, 20260720]

SIGNALS = {
    "GPS_L1CA": {
        "title": "GPS L1CA",
        "code": "GPSL1CA",
        "pull_in_db_hz": 22.0,
        "unaided_db_hz": 12.0,
        "aided_db_hz": 7.0,
    },
    "BDS_B1I": {
        "title": "BDS B1I",
        "code": "BDSB1I",
        "pull_in_db_hz": 24.0,
        "unaided_db_hz": 12.0,
        "aided_db_hz": 7.0,
    },
    "GPS_L5": {
        "title": "GPS L5",
        "code": "GPSL5",
        "pull_in_db_hz": 28.0,
        "unaided_db_hz": 12.0,
        "aided_db_hz": 7.0,
    },
}

SCENARIOS = (
    {
        "index": "01",
        "slug": "pull_in_sensitivity",
        "title": "牵引灵敏度",
        "duration_s": 120.0,
        "seeds": SEEDS_5,
        "purpose": "验证无同步、无电文辅助时从捕获结果移交到稳定跟踪的能力。",
        "input": "40、30 dB-Hz、目标牵引边界及边界以下1 dB；每档独立冷启动。",
        "truth": "捕获多普勒和码相位含规定移交误差，信号全程叠加 GOOD_TCXO_V1。",
        "expected": "边界及以上全部种子完成同步和PullIn移交；下一低1 dB至少留一组失败或边界记录。",
    },
    {
        "index": "02",
        "slug": "sustained_unaided",
        "title": "无电文辅助持续跟踪",
        "duration_s": 960.0,
        "seeds": SEEDS_5,
        "purpose": "测量只依赖接收机同步和自主符号处理时的持续跟踪灵敏度。",
        "input": "30 dB-Hz预热60秒，随后降到无辅助目标强度并保持900秒。",
        "truth": "不提供导航位正负号；位边界可由接收机自行获得。",
        "expected": "不重捕、不丢同步，尾段载波和码相位误差满足统一门限。",
    },
    {
        "index": "03",
        "slug": "sustained_aided",
        "title": "已知电文辅助持续跟踪",
        "duration_s": 960.0,
        "seeds": SEEDS_5,
        "purpose": "测量已知电文位值和位索引时可用于灵敏度声明的持续跟踪边界。",
        "input": "30 dB-Hz预热60秒，随后降到已知位辅助目标强度并保持900秒。",
        "truth": "提供与StarGen完全一致的位值、位索引和时间映射。",
        "expected": "5个固定种子全部保持跟踪；下一低1 dB至少补测一次。",
    },
    {
        "index": "04",
        "slug": "doppler_dynamics",
        "title": "多普勒动态能力",
        "duration_s": 900.0,
        "seeds": SEEDS_3,
        "purpose": "确定不同灵敏度下能够稳定承受的最大瞬时频率变化率。",
        "input": "扫描0、0.1、0.25、0.5、0.75和1 Hz/s，使用有界正弦动态而非无限斜升。",
        "truth": "GOOD_TCXO_V1基础扰动叠加指定最大频率变化率。",
        "expected": "逐灵敏度给出最大通过频漂，失败边界保留为回归基线。",
    },
    {
        "index": "05",
        "slug": "step_transitions",
        "title": "强弱阶跃切换",
        "duration_s": 900.0,
        "seeds": SEEDS_3,
        "purpose": "验证强、中、弱、极弱和恢复过程中的状态响应及瞬态稳定性。",
        "input": "强信号到中信号、弱信号、极弱信号，再恢复到强信号。",
        "truth": "C/N0按固定时刻阶跃，载波、码、数据位和噪声序列连续。",
        "expected": "状态只在门限确认后切换，切换期间环路不发散且恢复后回到稳态。",
    },
    {
        "index": "06",
        "slug": "slow_fade_recovery",
        "title": "缓慢遮挡与恢复",
        "duration_s": 900.0,
        "seeds": SEEDS_3,
        "purpose": "模拟建筑物或植被遮挡造成的缓慢衰减、驻留和恢复。",
        "input": "40 dB-Hz线性下降到目标极弱强度，保持后再线性恢复。",
        "truth": "信号幅度连续变化，噪声密度、载波和码相位连续。",
        "expected": "无漏切换、无反复振荡；恢复延迟符合估计窗口和确认时间。",
    },
    {
        "index": "07",
        "slug": "threshold_hysteresis",
        "title": "状态门限徘徊",
        "duration_s": 900.0,
        "seeds": SEEDS_3,
        "purpose": "验证C/N0在状态门限附近波动时的迟滞和抗抖动能力。",
        "input": "在每个强弱切换门限上下交替变化并保持足够长时间。",
        "truth": "使用连续噪声序列和GOOD_TCXO_V1，不重置信号相位。",
        "expected": "不出现高频状态振荡；每次转换均有可解释的门限穿越和确认延迟。",
    },
    {
        "index": "08",
        "slug": "endurance",
        "title": "一小时耐久测试",
        "duration_s": 3600.0,
        "seeds": SEEDS_3,
        "purpose": "验证灵敏度边界下的长期数值稳定性、同步保持和误差漂移。",
        "input": "分别在牵引、无辅助持续和已知位辅助三项边界运行3600秒。",
        "truth": "全程GOOD_TCXO_V1，实时二进制管道，不保存原始样点文件。",
        "expected": "无长期失锁、异常周跳或持续漂移，观测有效率满足统一门限。",
    },
)

CLOCK_PROFILE = {
    "id": "GOOD_TCXO_V1",
    "linear_doppler_rate_hz_s": 0.020,
    "doppler_jerk_hz_s2": 0.000020,
    "sine_amplitude_hz": 0.50,
    "sine_period_s": 120.0,
}

ACCEPTANCE = {
    "no_reacquisition": True,
    "no_sync_loss": True,
    "min_carrier_valid_ratio": 0.95,
    "max_doppler_rms_hz": 5.0,
    "max_doppler_p95_hz": 10.0,
    "max_code_phase_p95_chips": 0.20,
}


def structured_input(signal, scenario):
    """返回可由测试运行器直接展开的外部输入矩阵。"""
    slug = scenario["slug"]
    pull_in = signal["pull_in_db_hz"]
    unaided = signal["unaided_db_hz"]
    aided = signal["aided_db_hz"]
    frequency_error = 31.25 if signal["code"] == "GPSL5" else 62.5
    common = {
        "stream_format": "binary 3-bit I/Q",
        "acquisition_frequency_errors_hz": [
            -frequency_error, 0.0, frequency_error],
        "acquisition_code_errors_chips": [-0.3, 0.0, 0.3],
    }
    if slug == "pull_in_sensitivity":
        common.update({
            "cn0_levels_db_hz": [40.0, 30.0, pull_in, pull_in - 1.0],
            "assume_sync": False,
            "bit_aid": "none",
        })
    elif slug == "sustained_unaided":
        common.update({
            "cn0_schedule": [
                {"start_s": 0.0, "cn0_db_hz": 30.0},
                {"start_s": 60.0, "cn0_db_hz": unaided},
            ],
            "assume_sync": True,
            "bit_aid": "none",
            "below_boundary_probe_db_hz": unaided - 1.0,
        })
    elif slug == "sustained_aided":
        common.update({
            "cn0_schedule": [
                {"start_s": 0.0, "cn0_db_hz": 30.0},
                {"start_s": 60.0, "cn0_db_hz": aided},
            ],
            "assume_sync": True,
            "bit_aid": "known",
            "below_boundary_probe_db_hz": aided - 1.0,
        })
    elif slug == "doppler_dynamics":
        common.update({
            "cn0_levels_db_hz": [40.0, 30.0, unaided, aided],
            "max_doppler_rate_levels_hz_s": [
                0.0, 0.1, 0.25, 0.5, 0.75, 1.0],
            "dynamic_model": "bounded_sine",
            "bit_aid_by_level": "none_then_known_at_aided_boundary",
        })
    elif slug == "step_transitions":
        common.update({
            "cn0_mode": "step",
            "cn0_schedule": [
                {"start_s": 0.0, "cn0_db_hz": 40.0},
                {"start_s": 180.0, "cn0_db_hz": 30.0},
                {"start_s": 360.0, "cn0_db_hz": 18.0},
                {"start_s": 540.0, "cn0_db_hz": aided},
                {"start_s": 720.0, "cn0_db_hz": 40.0},
            ],
        })
    elif slug == "slow_fade_recovery":
        common.update({
            "cn0_mode": "linear",
            "cn0_schedule": [
                {"start_s": 0.0, "cn0_db_hz": 40.0},
                {"start_s": 180.0, "cn0_db_hz": 40.0},
                {"start_s": 420.0, "cn0_db_hz": aided},
                {"start_s": 600.0, "cn0_db_hz": aided},
                {"start_s": 840.0, "cn0_db_hz": 40.0},
                {"start_s": 900.0, "cn0_db_hz": 40.0},
            ],
        })
    elif slug == "threshold_hysteresis":
        common.update({
            "cn0_mode": "step",
            "cn0_schedule": [
                {"start_s": 0.0, "cn0_db_hz": 40.0},
                {"start_s": 150.0, "cn0_db_hz": 31.0},
                {"start_s": 270.0, "cn0_db_hz": 29.0},
                {"start_s": 390.0, "cn0_db_hz": 19.0},
                {"start_s": 510.0, "cn0_db_hz": 17.0},
                {"start_s": 630.0, "cn0_db_hz": 13.0},
                {"start_s": 750.0, "cn0_db_hz": 15.5},
                {"start_s": 870.0, "cn0_db_hz": 33.0},
            ],
        })
    else:
        common.update({
            "operating_points": [
                {"name": "pull_in_boundary", "cn0_db_hz": pull_in,
                 "bit_aid": "none"},
                {"name": "unaided_boundary", "cn0_db_hz": unaided,
                 "bit_aid": "none"},
                {"name": "aided_boundary", "cn0_db_hz": aided,
                 "bit_aid": "known"},
            ],
        })
    return common


def scenario_payload(signal_id, signal, scenario):
    """建立一个不含算法细节的固定场景定义。"""
    case_id = "ST-{}-{}-{}".format(
        signal["code"], scenario["index"], scenario["slug"].upper())
    return {
        "schema_version": 1,
        "case_id": case_id,
        "test_set": "Qualification",
        "signal": signal_id,
        "category": scenario["slug"],
        "source": "StarGen realtime binary pipe",
        "duration_s": scenario["duration_s"],
        "seeds": scenario["seeds"],
        "clock_profile": CLOCK_PROFILE,
        "sensitivity_targets_db_hz": {
            "pull_in": signal["pull_in_db_hz"],
            "sustained_unaided": signal["unaided_db_hz"],
            "sustained_aided": signal["aided_db_hz"],
        },
        "input": structured_input(signal, scenario),
        "input_description": scenario["input"],
        "truth_description": scenario["truth"],
        "acceptance": ACCEPTANCE,
        "required_outputs": [
            "summary.json",
            "metrics.csv",
            "seed-*/observations.csv",
            "seed-*/state_events.csv",
            "figures/*.png",
        ],
    }


def scenario_readme(signal, scenario, payload):
    """生成一个场景的固定中文说明。"""
    return """# {signal_title} - {scenario_title}

固定案例 ID：`{case_id}`

## 现实场景

{purpose}

## 输入

- 信号：`{signal_title}`
- 数据源：StarGen 实时二进制管道
- 单次时长：`{duration:g} s`
- 固定种子：`{seeds}`
- 输入过程：{input_text}

## 真值

{truth_text}

名义时钟使用 `GOOD_TCXO_V1`：线性频漂 `0.020 Hz/s`、加加速度
`0.000020 Hz/s^2`、慢周期扰动 `0.50 Hz / 120 s`。

## 预期结果

{expected}

统一精度门限为：载波有效观测率不低于 `95%`，多普勒 RMS 不超过
`5 Hz`、P95 不超过 `10 Hz`，动态真实码相位 P95 不超过 `0.20 chip`。

## 实际结果

尚未在当前固定案例版本上发布 Qualification 运行。结果将保存在
`runs/startrack-<commit>_<profile-version>/`，运行时间只写入
`summary.json`，不会改变案例 ID 或目录。

## 结论

待固定种子运行完成后填写。失败结果不会删除，它将作为下一版本的回归
基线保留。
""".format(
        signal_title=signal["title"],
        scenario_title=scenario["title"],
        case_id=payload["case_id"],
        purpose=scenario["purpose"],
        duration=scenario["duration_s"],
        seeds=", ".join(str(seed) for seed in scenario["seeds"]),
        input_text=scenario["input"],
        truth_text=scenario["truth"],
        expected=scenario["expected"],
    )


def signal_readme(signal_id, signal):
    """生成信号根目录的灵敏度与历史对比首页。"""
    rows = []
    for scenario in SCENARIOS:
        folder = "{}_{}".format(scenario["index"], scenario["slug"])
        rows.append("| [{}]({}/README.md) | {} s | 待运行 |".format(
            scenario["title"], folder, int(scenario["duration_s"])))
    return """# {title} Qualification 基准

## 三项灵敏度

下表中的目标值用于固定测试点选择，不等同于已通过 Qualification 的
正式结论。只有5个固定种子全部通过后，才填写“当前合格值”。

| 指标 | 目标 C/N0 | 等效功率 | 当前合格值 |
|---|---:|---:|---:|
| 牵引灵敏度 | {pull:g} dB-Hz | {pull_dbm:g} dBm | 待运行 |
| 无电文辅助持续灵敏度 | {unaided:g} dB-Hz | {unaided_dbm:g} dBm | 待运行 |
| 已知电文辅助持续灵敏度 | {aided:g} dB-Hz | {aided_dbm:g} dBm | 待运行 |

功率按有效噪声密度 `-170 dBm/Hz` 换算。

## 固定场景

| 场景 | 单次时长 | 当前结论 |
|---|---:|---|
{rows}

## 状态与动态结论

- 最大通过频漂：待 `04_doppler_dynamics` 完成后填写。
- 阶跃状态切换：待 `05_step_transitions` 完成后填写。
- 缓慢遮挡恢复：待 `06_slow_fade_recovery` 完成后填写。
- 一小时耐久：待 `08_endurance` 完成后填写。

## 版本对比

| StarTrack版本 | 档案版本 | 受影响场景 | 指标变化 | 结论 |
|---|---|---|---|---|
| 待首次固定基准 | v1 | 全部 | 尚无可比数据 | 待运行 |

每次算法更新只在本表追加一行，并把新结果放入同一固定场景的 `runs/`
目录；不再按日期复制测试体系。
""".format(
        title=signal["title"],
        pull=signal["pull_in_db_hz"],
        unaided=signal["unaided_db_hz"],
        aided=signal["aided_db_hz"],
        pull_dbm=signal["pull_in_db_hz"] - 170.0,
        unaided_dbm=signal["unaided_db_hz"] - 170.0,
        aided_dbm=signal["aided_db_hz"] - 170.0,
        rows="\n".join(rows),
    )


def write(path, text, force):
    """创建UTF-8文本；默认不覆盖人工补充过的结果说明。"""
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def scaffold(force=False):
    """生成三个信号、八类场景及空运行目录。"""
    for signal_id, signal in SIGNALS.items():
        signal_root = STARTRACK_ROOT / signal_id
        write(signal_root / "README.md",
              signal_readme(signal_id, signal), force)
        for scenario in SCENARIOS:
            folder = "{}_{}".format(scenario["index"], scenario["slug"])
            scenario_root = signal_root / folder
            payload = scenario_payload(signal_id, signal, scenario)
            write(scenario_root / "README.md",
                  scenario_readme(signal, scenario, payload), force)
            write(scenario_root / "scenario.json",
                  json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                  force)
            runs = scenario_root / "runs"
            runs.mkdir(parents=True, exist_ok=True)
            write(runs / ".gitkeep", "", False)


def main():
    """解析覆盖开关并生成目录。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    scaffold(args.force)
    print("Scaffolded {} signals x {} fixed scenarios".format(
        len(SIGNALS), len(SCENARIOS)))


if __name__ == "__main__":
    main()
