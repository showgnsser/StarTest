# 16 dB-Hz weak-signal hold - seed 20260715

## 测试目的

Measure weak-signal tracking stability under continuous TCXO-equivalent dynamics.

## 输入

- 信号：BDS B1I D1，PRN 6，7.68 Msps，零中频，3-bit I/Q。
- 数据链路：StarGen 实时二进制管道输入 StarTrack，不生成中间信号文件。
- 时长与种子：900 s，seed 20260715。
- C/N0：Step，0s:16dB-Hz。
- 多普勒动态：线性 0.020 Hz/s，叠加幅度 0.50 Hz、周期 120 s 的慢变化。
- 已知电文：否。
- 自动状态切换：关闭。

## 预期结果

Track for 900 s without divergence; tail frequency P95 <= 5 Hz and code P95 <= 0.2 chip.

## 实际结果

- 总体结论：**PASS**。
- 跟踪验收：PASS；C/N0 监测验收：PASS。
- 状态路径：`Weak`。
- 末段多普勒 RMS / P95 / 最大绝对误差：0.4106 / 0.8442 / 1.1679 Hz。
- 末段码相位 MAE / P95 / 最大绝对误差：0.0202 / 0.0473 / 0.0618 chip。
- C/N0 偏差 / RMSE / 有效率：-0.795 / 0.892 dB / 1.000。
- 回捕次数：0；切换后发散次数：0。
- 仿真墙钟耗时：132.72 s，处理速度为实时的 6.78 倍。

## 结论

该案例满足公开验收要求。`WARN` 表示跟踪本身稳定，但低 C/N0 监测值的有效率或误差未达到监测门限；失败案例保留为当前能力边界和后续回归基准。

## 文件

- `scenario.json`：外部输入与预期结果。
- `observations.csv`：1 Hz 黑盒观测。
- `state_events.csv`：状态与同步事件。
- `result.json`：公开指标和状态轨迹。
- `tracking.png`：码相位、频率、PLI 与 C/N0 图。
