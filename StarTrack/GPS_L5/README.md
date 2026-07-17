# GPS L5 Qualification 基准

## 三项灵敏度

下表中的目标值用于固定测试点选择，不等同于已通过 Qualification 的
正式结论。只有5个固定种子全部通过后，才填写“当前合格值”。

| 指标 | 目标 C/N0 | 等效功率 | 当前合格值 |
|---|---:|---:|---:|
| 牵引灵敏度 | 28 dB-Hz | -142 dBm | 28 dB-Hz / -142 dBm |
| 无电文辅助持续灵敏度 | 12 dB-Hz | -158 dBm | 待运行 |
| 已知电文辅助持续灵敏度 | 7 dB-Hz | -163 dBm | 待运行 |

功率按有效噪声密度 `-170 dBm/Hz` 换算。

## 固定场景

| 场景 | 单次时长 | 当前结论 |
|---|---:|---|
| [牵引灵敏度](01_pull_in_sensitivity/README.md) | 120 s | 5/5 通过 |
| [无电文辅助持续跟踪](02_sustained_unaided/README.md) | 960 s | 待运行 |
| [已知电文辅助持续跟踪](03_sustained_aided/README.md) | 960 s | 待运行 |
| [多普勒动态能力](04_doppler_dynamics/README.md) | 900 s | 待运行 |
| [强弱阶跃切换](05_step_transitions/README.md) | 900 s | 待运行 |
| [缓慢遮挡与恢复](06_slow_fade_recovery/README.md) | 900 s | 待运行 |
| [状态门限徘徊](07_threshold_hysteresis/README.md) | 900 s | 待运行 |
| [一小时耐久测试](08_endurance/README.md) | 3600 s | 待运行 |

## 状态与动态结论

- 最大通过频漂：待 `04_doppler_dynamics` 完成后填写。
- 阶跃状态切换：待 `05_step_transitions` 完成后填写。
- 缓慢遮挡恢复：待 `06_slow_fade_recovery` 完成后填写。
- 一小时耐久：待 `08_endurance` 完成后填写。

## 版本对比

| StarTrack版本 | 档案版本 | 受影响场景 | 指标变化 | 结论 |
|---|---|---|---|---|
| `503cdea` | pullin-v2 | 牵引灵敏度 | 首次固定五种子边界基准 | 5/5 通过 |

每次算法更新只在本表追加一行，并把新结果放入同一固定场景的 `runs/`
目录；不再按日期复制测试体系。
