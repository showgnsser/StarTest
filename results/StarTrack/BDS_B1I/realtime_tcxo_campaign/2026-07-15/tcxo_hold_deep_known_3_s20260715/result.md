# 3 dB-Hz known-bit limit probe - seed 20260715

## 测试目的

Identify the point at which the current BDS B1I known-bit implementation no longer remains stable.

## 输入

- 信号：BDS B1I D1，PRN 6，7.68 Msps，零中频，3-bit I/Q。
- 数据链路：StarGen 实时二进制管道输入 StarTrack，不生成中间信号文件。
- 时长与种子：900 s，seed 20260715。
- C/N0：Step，0s:3dB-Hz。
- 多普勒动态：线性 0.020 Hz/s，叠加幅度 0.50 Hz、周期 120 s 的慢变化。
- 已知电文：是。
- 自动状态切换：关闭。

## 预期结果

Exploratory limit case; failure is retained as boundary evidence.

## 实际结果

- 总体结论：**FAIL**。
- 跟踪验收：FAIL；C/N0 监测验收：WARN。
- 状态路径：`Deep`。
- 末段多普勒 RMS / P95 / 最大绝对误差：167.6099 / 195.5707 / 197.1059 Hz。
- 末段码相位 MAE / P95 / 最大绝对误差：42.9893 / 73.5112 / 77.2619 chip。
- C/N0 偏差 / RMSE / 有效率：-1.999 / 4.025 dB / 0.495。
- 回捕次数：0；切换后发散次数：0。
- 仿真墙钟耗时：121.97 s，处理速度为实时的 7.38 倍。

## 结论

该案例未完全满足公开验收要求。`WARN` 表示跟踪本身稳定，但低 C/N0 监测值的有效率或误差未达到监测门限；失败案例保留为当前能力边界和后续回归基准。

## 文件

- `scenario.json`：外部输入与预期结果。
- `observations.csv`：1 Hz 黑盒观测。
- `state_events.csv`：状态与同步事件。
- `result.json`：公开指标和状态轨迹。
- `tracking.png`：码相位、频率、PLI 与 C/N0 图。
