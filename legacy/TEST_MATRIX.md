# StarTrack 测试用例矩阵

> 更新日期：2026-07-16。本页由 `tools/build_test_matrix.py` 从公开结果自动生成。

该矩阵只汇总测试场景、外部输入、公开输出和验收结论。算法原理与内部参数请查阅 StarTrack 仓库。

## 总览

| 信号 | 用例数 |
|---|---:|
| BDS_B1I | 30 |
| GPS_L1CA | 25 |
| GPS_L5 | 19 |

共 74 个用例：通过 65，失败 9，仅记录 0。

失败用例不会删除，它们是边界和回归测试的重要基线。

## BDS_B1I

| 日期 | 测试集 | 用例 | 时长 | 种子 | C/N0 dB-Hz | 初始状态 | 结果 | 关键输出 | 详情 |
|---|---|---|---:|---:|---|---|---|---|---|
| 2026-07-16 | adaptive_kalman | akf_adaptive_40_3_40_s20260715 | 900 s | 20260715 | 40 -> 3 -> 40 | PullIn | 通过 | 频差RMS 2.9246 Hz；码差P95 0.1014 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_adaptive_40_3_40_s20260715/result.md) |
| 2026-07-16 | adaptive_kalman | akf_adaptive_40_to_7_s20260715 | 900 s | 20260715 | 40 -> 7 | PullIn | 通过 | 频差RMS 1.5144 Hz；码差P95 0.1438 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_adaptive_40_to_7_s20260715/result.md) |
| 2026-07-16 | adaptive_kalman | akf_adaptive_strong_40_s20260715 | 900 s | 20260715 | 40 | PullIn | 通过 | 频差RMS 0.0089 Hz；码差P95 0.0037 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_adaptive_strong_40_s20260715/result.md) |
| 2026-07-16 | adaptive_kalman | akf_fixed_40_3_40_s20260715 | 900 s | 20260715 | 40 -> 3 -> 40 | PullIn | 通过 | 频差RMS 3.2503 Hz；码差P95 0.1014 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_fixed_40_3_40_s20260715/result.md) |
| 2026-07-16 | adaptive_kalman | akf_fixed_40_to_7_s20260715 | 900 s | 20260715 | 40 -> 7 | PullIn | 通过 | 频差RMS 1.5144 Hz；码差P95 0.1438 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_fixed_40_to_7_s20260715/result.md) |
| 2026-07-16 | adaptive_kalman | akf_fixed_strong_40_s20260715 | 900 s | 20260715 | 40 | PullIn | 通过 | 频差RMS 0.0089 Hz；码差P95 0.0037 chip | [查看](results/StarTrack/BDS_B1I/adaptive_kalman/2026-07-16/akf_fixed_strong_40_s20260715/result.md) |
| 2026-07-16 | pll_pli_diagnostic | steady_40_seed20260716 | 900 s | 20260716 | 40 | - | 通过 | 频差RMS 0.2252 Hz；码差P95 0.0034 chip | [查看](results/StarTrack/BDS_B1I/pll_pli_diagnostic/2026-07-16/steady_40_seed20260716/result.md) |
| 2026-07-16 | pll_pli_diagnostic | transition_40_24_16_12_7_16_40_seed20260716 | 900 s | 20260716 | 40 -> 24 -> 16 -> 12 -> 7 -> 16 -> 40 | - | 通过 | 频差RMS 0.2501 Hz；码差P95 0.0280 chip | [查看](results/StarTrack/BDS_B1I/pll_pli_diagnostic/2026-07-16/transition_40_24_16_12_7_16_40_seed20260716/result.md) |
| 2026-07-14 | power_transitions | repeated_slow_fades | 450 s | 20260714 | 40 -> 12 -> 40 -> 12 -> 40 | - | 通过 | 频差RMS 0.0278 Hz；码差P95 0.0055 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/repeated_slow_fades/result.md) |
| 2026-07-14 | power_transitions | short_shadow_5s | 150 s | 20260714 | 40 -> 10 -> 40 | - | 通过 | 频差RMS 0.0320 Hz；码差P95 0.0069 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/short_shadow_5s/result.md) |
| 2026-07-14 | power_transitions | slow_deep_fade | 480 s | 20260714 | 40 -> 10 -> 40 | - | 通过 | 频差RMS 0.0061 Hz；码差P95 0.0034 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/slow_deep_fade/result.md) |
| 2026-07-14 | power_transitions | slow_fade_drift_0p1 | 360 s | 20260714 | 40 -> 10 -> 40 | - | 通过 | 频差RMS 0.0315 Hz；码差P95 0.0028 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/slow_fade_drift_0p1/result.md) |
| 2026-07-14 | power_transitions | steady_strong_40 | 90 s | 20260714 | 40 | - | 通过 | 频差RMS 0.0409 Hz；码差P95 0.0036 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/steady_strong_40/result.md) |
| 2026-07-14 | power_transitions | step_deep_fade | 220 s | 20260714 | 40 -> 10 -> 40 | - | 通过 | 频差RMS 0.0386 Hz；码差P95 0.0030 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/step_deep_fade/result.md) |
| 2026-07-14 | power_transitions | threshold_ramp | 480 s | 20260714 | 40 -> 17 -> 23 -> 40 | - | 通过 | 频差RMS 0.0333 Hz；码差P95 0.0040 chip | [查看](results/StarTrack/BDS_B1I/power_transitions/2026-07-14/threshold_ramp/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_slow_40_7_40_s20260715 | 900 s | 20260715 | 40 -> 7 -> 40 | PullIn | 通过 | 频差RMS 0.1585 Hz；码差P95 0.0182 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_slow_40_7_40_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_slow_40_7_40_s20260716 | 900 s | 20260716 | 40 -> 7 -> 40 | PullIn | 通过 | 频差RMS 0.1758 Hz；码差P95 0.0156 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_slow_40_7_40_s20260716/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_slow_40_7_40_s20260717 | 900 s | 20260717 | 40 -> 7 -> 40 | PullIn | 通过 | 频差RMS 0.1577 Hz；码差P95 0.0172 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_slow_40_7_40_s20260717/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_steady_40_s20260715 | 900 s | 20260715 | 40 | PullIn | 通过 | 频差RMS 0.2247 Hz；码差P95 0.0029 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_steady_40_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_step_40_24_16_12_7_16_40_s20260715 | 900 s | 20260715 | 40 -> 24 -> 16 -> 12 -> 7 -> 16 -> 40 | PullIn | 通过 | 频差RMS 0.2664 Hz；码差P95 0.0432 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_step_40_24_16_12_7_16_40_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_auto_threshold_dwell_s20260715 | 900 s | 20260715 | 40 -> 29 -> 19 -> 17 -> 14 -> 12.5 -> 15.5 -> 33 | PullIn | 通过 | 频差RMS 0.1294 Hz；码差P95 0.0336 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_auto_threshold_dwell_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_known_3_s20260715 | 900 s | 20260715 | 3 | Deep | 失败 | 频差RMS 167.6099 Hz；码差P95 73.5112 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_known_3_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_known_5_s20260715 | 900 s | 20260715 | 5 | Deep | 通过 | 频差RMS 0.7268 Hz；码差P95 0.1154 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_known_5_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_known_7_s20260715 | 900 s | 20260715 | 7 | Deep | 通过 | 频差RMS 0.4326 Hz；码差P95 0.0600 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_known_7_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_known_7_s20260716 | 900 s | 20260716 | 7 | Deep | 通过 | 频差RMS 0.4501 Hz；码差P95 0.0966 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_known_7_s20260716/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_known_7_s20260717 | 900 s | 20260717 | 7 | Deep | 通过 | 频差RMS 0.4955 Hz；码差P95 0.0837 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_known_7_s20260717/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_soft_10_s20260715 | 900 s | 20260715 | 10 | Deep | 失败 | 频差RMS 77.0644 Hz；码差P95 40.5874 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_soft_10_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_deep_soft_12_s20260715 | 900 s | 20260715 | 12 | Deep | 通过 | 频差RMS 1.5277 Hz；码差P95 0.1570 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_deep_soft_12_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_medium_24_s20260715 | 900 s | 20260715 | 24 | Medium | 通过 | 频差RMS 0.2966 Hz；码差P95 0.0278 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_medium_24_s20260715/result.md) |
| 2026-07-15 | realtime_tcxo_campaign | tcxo_hold_weak_16_s20260715 | 900 s | 20260715 | 16 | Weak | 通过 | 频差RMS 0.4106 Hz；码差P95 0.0473 chip | [查看](results/StarTrack/BDS_B1I/realtime_tcxo_campaign/2026-07-15/tcxo_hold_weak_16_s20260715/result.md) |

## GPS_L1CA

| 日期 | 测试集 | 用例 | 时长 | 种子 | C/N0 dB-Hz | 初始状态 | 结果 | 关键输出 | 详情 |
|---|---|---|---:|---:|---|---|---|---|---|
| 2026-07-16 | cross_signal_regression | pullin_24_60s | 60 s | 20260717 | 24 | - | 通过 | 频差RMS 0.2740 Hz；码差P95 0.0104 chip | [查看](results/StarTrack/GPS_L1CA/cross_signal_regression/2026-07-16/pullin_24_60s/result.md) |
| 2026-07-16 | cross_signal_regression | slowfade_40_10_40_900s | 900 s | 20260718 | - | - | 失败 | 频差RMS 110.9100 Hz；码差P95 58.3000 chip | [查看](results/StarTrack/GPS_L1CA/cross_signal_regression/2026-07-16/slowfade_40_10_40_900s/result.md) |
| 2026-07-16 | cross_signal_regression | strong_40_30s | 30 s | 20260716 | 40 | - | 通过 | 频差RMS 0.2600 Hz；码差P95 0.0077 chip | [查看](results/StarTrack/GPS_L1CA/cross_signal_regression/2026-07-16/strong_40_30s/result.md) |
| 2026-07-16 | cross_signal_regression | transition_40_12_40_210s | 210 s | 20260716 | - | - | 通过 | 频差RMS 0.3060 Hz；码差P95 0.0124 chip | [查看](results/StarTrack/GPS_L1CA/cross_signal_regression/2026-07-16/transition_40_12_40_210s/result.md) |
| 2026-07-16 | state_sensitivity_matrix | aided_known_24_s20260719 | 300 s | 20260719 | 24 | Aided | 通过 | 频差RMS 0.0660 Hz；码差P95 0.0220 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/aided_known_24_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_ramp_40_12_40_s20260719 | 600 s | 20260719 | 40 -> 12 -> 40 | PullIn | 通过 | 频差RMS 0.1540 Hz；码差P95 0.0647 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/auto_ramp_40_12_40_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_ramp_40_12_40_unaided_s20260719 | 600 s | 20260719 | 40 -> 12 -> 40 | PullIn | 失败 | 频差RMS 15.5850 Hz；码差P95 0.0754 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/auto_ramp_40_12_40_unaided_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_short_shadows_s20260719 | 540 s | 20260719 | 40 -> 14 -> 40 -> 14 -> 40 -> 14 -> 40 | PullIn | 通过 | 频差RMS 0.5990 Hz；码差P95 0.0253 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/auto_short_shadows_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_step_40_24_18_14_40_s20260719 | 540 s | 20260719 | 40 -> 24 -> 18 -> 14 -> 24 -> 40 | PullIn | 通过 | 频差RMS 0.1960 Hz；码差P95 0.0505 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/auto_step_40_24_18_14_40_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | deep_known_3_s20260719 | 300 s | 20260719 | 3 | Deep | 通过 | 频差RMS 1.7850 Hz；码差P95 0.1522 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/deep_known_3_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | deep_soft_12_s20260719 | 300 s | 20260719 | 12 | Deep | 失败 | 频差RMS 10.0000 Hz；码差P95 0.1856 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/deep_soft_12_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | deep_soft_14_s20260719 | 300 s | 20260719 | 14 | Deep | 通过 | 频差RMS 0.3920 Hz；码差P95 0.0303 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/deep_soft_14_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | lock_28_s20260719 | 300 s | 20260719 | 28 | Lock | 通过 | 频差RMS 0.3820 Hz；码差P95 0.0366 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/lock_28_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | lock_30_s20260719 | 300 s | 20260719 | 30 | Lock | 通过 | 频差RMS 0.2960 Hz；码差P95 0.0299 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/lock_30_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longfast_24_s20260719 | 300 s | 20260719 | 24 | LongFast | 通过 | 频差RMS 0.7390 Hz；码差P95 0.0753 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/longfast_24_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longfast_26_s20260719 | 300 s | 20260719 | 26 | LongFast | 通过 | 频差RMS 0.3530 Hz；码差P95 0.0631 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/longfast_26_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longlock_20_s20260719 | 300 s | 20260719 | 20 | LongLock | 通过 | 频差RMS 1.5650 Hz；码差P95 0.0822 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/longlock_20_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longlock_22_s20260719 | 300 s | 20260719 | 22 | LongLock | 通过 | 频差RMS 0.8110 Hz；码差P95 0.0643 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/longlock_22_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | medium_16_s20260719 | 300 s | 20260719 | 16 | Medium | 失败 | 频差RMS 27.9540 Hz；码差P95 0.6531 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/medium_16_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | medium_18_s20260719 | 300 s | 20260719 | 18 | Medium | 通过 | 频差RMS 1.7200 Hz；码差P95 0.0519 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/medium_18_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | pullin_24_s20260719 | 300 s | 20260719 | 24 | PullIn | 通过 | 频差RMS 0.3180 Hz；码差P95 0.0231 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/pullin_24_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | strong_26_s20260719 | 300 s | 20260719 | 26 | Strong | 通过 | 频差RMS 0.3700 Hz；码差P95 0.0176 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/strong_26_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | strong_30_s20260719 | 300 s | 20260719 | 30 | Strong | 通过 | 频差RMS 0.2210 Hz；码差P95 0.0105 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/strong_30_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | weak_14_s20260719 | 300 s | 20260719 | 14 | Weak | 通过 | 频差RMS 0.5490 Hz；码差P95 0.0480 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/weak_14_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | weak_16_s20260719 | 300 s | 20260719 | 16 | Weak | 通过 | 频差RMS 0.4370 Hz；码差P95 0.0355 chip | [查看](results/StarTrack/GPS_L1CA/state_sensitivity_matrix/2026-07-16/weak_16_s20260719/result.md) |

## GPS_L5

| 日期 | 测试集 | 用例 | 时长 | 种子 | C/N0 dB-Hz | 初始状态 | 结果 | 关键输出 | 详情 |
|---|---|---|---:|---:|---|---|---|---|---|
| 2026-07-16 | cross_signal_regression | pullin_28_60s | 60 s | 20260717 | 28 | - | 通过 | 频差RMS 0.1310 Hz；码差P95 0.0092 chip | [查看](results/StarTrack/GPS_L5/cross_signal_regression/2026-07-16/pullin_28_60s/result.md) |
| 2026-07-16 | cross_signal_regression | slowfade_40_10_40_900s | 900 s | 20260718 | - | - | 失败 | 频差RMS 33.7100 Hz；码差P95 413.9100 chip | [查看](results/StarTrack/GPS_L5/cross_signal_regression/2026-07-16/slowfade_40_10_40_900s/result.md) |
| 2026-07-16 | cross_signal_regression | strong_40_30s | 30 s | 20260716 | 40 | - | 通过 | 频差RMS 0.0920 Hz；码差P95 0.0198 chip | [查看](results/StarTrack/GPS_L5/cross_signal_regression/2026-07-16/strong_40_30s/result.md) |
| 2026-07-16 | cross_signal_regression | transition_40_12_40_210s | 210 s | 20260716 | - | - | 通过 | 频差RMS 0.8630 Hz；码差P95 0.0987 chip | [查看](results/StarTrack/GPS_L5/cross_signal_regression/2026-07-16/transition_40_12_40_210s/result.md) |
| 2026-07-16 | state_sensitivity_matrix | aided_pilot_24_s20260719 | 300 s | 20260719 | 24 | Aided | 通过 | 频差RMS 0.0860 Hz；码差P95 0.0297 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/aided_pilot_24_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_ramp_40_12_40_s20260719 | 600 s | 20260719 | 40 -> 12 -> 40 | PullIn | 通过 | 频差RMS 0.2490 Hz；码差P95 0.1078 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/auto_ramp_40_12_40_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_short_shadows_s20260719 | 540 s | 20260719 | 40 -> 14 -> 40 -> 14 -> 40 -> 14 -> 40 | PullIn | 通过 | 频差RMS 0.3920 Hz；码差P95 0.0881 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/auto_short_shadows_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | auto_step_40_28_18_14_40_s20260719 | 540 s | 20260719 | 40 -> 28 -> 18 -> 14 -> 28 -> 40 | PullIn | 通过 | 频差RMS 0.3140 Hz；码差P95 0.0955 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/auto_step_40_28_18_14_40_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | deep_pilot_10_s20260719 | 300 s | 20260719 | 10 | Deep | 失败 | 频差RMS 0.6300 Hz；码差P95 0.3152 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/deep_pilot_10_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | deep_pilot_12_s20260719 | 300 s | 20260719 | 12 | Deep | 通过 | 频差RMS 0.3370 Hz；码差P95 0.1237 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/deep_pilot_12_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | lock_28_s20260719 | 300 s | 20260719 | 28 | Lock | 通过 | 频差RMS 0.5250 Hz；码差P95 0.0607 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/lock_28_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longfast_24_s20260719 | 300 s | 20260719 | 24 | LongFast | 通过 | 频差RMS 0.7880 Hz；码差P95 0.1332 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/longfast_24_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | longlock_20_s20260719 | 300 s | 20260719 | 20 | LongLock | 通过 | 频差RMS 1.1840 Hz；码差P95 0.1220 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/longlock_20_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | medium_16_s20260719 | 300 s | 20260719 | 16 | Medium | 失败 | 频差RMS 3.1500 Hz；码差P95 0.3676 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/medium_16_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | medium_18_s20260719 | 300 s | 20260719 | 18 | Medium | 通过 | 频差RMS 1.5670 Hz；码差P95 0.1719 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/medium_18_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | pullin_28_s20260719 | 300 s | 20260719 | 28 | PullIn | 通过 | 频差RMS 0.1620 Hz；码差P95 0.0213 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/pullin_28_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | strong_26_s20260719 | 300 s | 20260719 | 26 | Strong | 通过 | 频差RMS 0.5020 Hz；码差P95 0.0314 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/strong_26_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | weak_14_s20260719 | 300 s | 20260719 | 14 | Weak | 通过 | 频差RMS 0.4040 Hz；码差P95 0.1159 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/weak_14_s20260719/result.md) |
| 2026-07-16 | state_sensitivity_matrix | weak_16_s20260719 | 300 s | 20260719 | 16 | Weak | 通过 | 频差RMS 0.3040 Hz；码差P95 0.0860 chip | [查看](results/StarTrack/GPS_L5/state_sensitivity_matrix/2026-07-16/weak_16_s20260719/result.md) |
