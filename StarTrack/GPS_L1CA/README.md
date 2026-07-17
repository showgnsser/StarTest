# GPS L1CA 固定测试基准

## 三项灵敏度

功率按有效噪声密度 `-170 dBm/Hz` 换算。Development 用于快速验证算法方向；只有固定五种子和规定时长全部通过后，才更新 Qualification 正式结论。

| 指标 | 目标 C/N0 | 等效功率 | 当前 Development | 当前 Qualification |
|---|---:|---:|---|---|
| 牵引灵敏度 | 22 dB-Hz | -148 dBm | 7/7 代表组合通过 | 22 dB-Hz，35/35 通过 |
| 无电文辅助持续灵敏度 | 10 dB-Hz | -160 dBm | 单种子 240 s 通过 | 待运行 |
| 已知电文辅助持续灵敏度 | 7 dB-Hz | -163 dBm | 单种子 240 s 通过 | 待运行 |

## 固定场景

| 场景 | 正式时长 | 最新 Development 结论 |
|---|---:|---|
| [牵引灵敏度](01_pull_in_sensitivity/README.md) | 120 s | 22/30/40 dB-Hz 共 7/7 通过 |
| [无电文辅助持续跟踪](02_sustained_unaided/README.md) | 960 s | 40/18/10 dB-Hz 共 3/3 通过 |
| [已知电文辅助持续跟踪](03_sustained_aided/README.md) | 960 s | 7 dB-Hz 通过 |
| [多普勒动态能力](04_doppler_dynamics/README.md) | 900 s | 必测 4/4 通过；7 dB-Hz 与 1 Hz/s 为失败边界 |
| [强弱阶跃切换](05_step_transitions/README.md) | 900 s | 300 s 压缩场景通过 |
| [缓慢遮挡与恢复](06_slow_fade_recovery/README.md) | 900 s | 300 s 压缩场景通过 |
| [状态门限迟滞](07_threshold_hysteresis/README.md) | 900 s | 300 s 压缩场景通过 |
| [一小时耐久测试](08_endurance/README.md) | 3600 s | 当前开发阶段暂不运行 |

## 状态与动态结论

- 强信号 PullIn 退出时间为 `1.48~1.50 s`，没有固定 30 秒等待。
- 22 dB-Hz 边界在代表性移交误差下退出时间为 `2.78~6.18 s`。
- 10 dB-Hz 无电文辅助持续跟踪通过，码相位 P95 为 `0.078 chip`。
- 7 dB-Hz 已知电文辅助持续跟踪通过，码相位 P95 为 `0.078 chip`。
- 30 dB-Hz 支持 `1 Hz/s`；10 dB-Hz 支持本次测试的 `0.25 Hz/s`。
- 7 dB-Hz 与 `1 Hz/s` 的组合失败，极限灵敏度与最大动态需分别标注。
- 阶跃、缓慢衰减和门限徘徊场景均未出现重新捕获或切换后持续发散。

## 版本对比

| StarTrack 版本 | 档案版本 | 受影响场景 | 指标变化 | 结论 |
|---|---|---|---|---|
| `503cdea` | pullin-v2 | 牵引灵敏度 | 首次固定五种子基准 | 22 dB-Hz，35/35 通过 |
| `0795a62` | l1ca-v3 | 牵引、持续、动态、切换 | 无辅助目标更新为 10 dB-Hz，并补齐七类 Development 回归 | 必测 19/19 通过，另保留 1 个探索性失败边界 |

新结果继续写入同一固定场景的 `runs/` 目录，不再按日期复制测试体系。
