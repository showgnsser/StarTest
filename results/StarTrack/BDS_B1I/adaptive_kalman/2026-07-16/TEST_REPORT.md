# BDS B1I 自适应跟踪 A/B 测试

## 测试目的

比较固定参数与自适应模式在强信号、强到弱、深衰落后恢复三类场景中的公开跟踪结果，
重点检查自适应模式是否引入稳态回归或状态切换发散。

## 公共输入

- 信号：BDS B1I D1，PRN 6。
- 输入：StarGen 到 StarTrack 实时二进制管道。
- 时长：每组900 s。
- 随机种子：20260715。
- 捕获移交误差：-62.5 Hz，+0.3 chip。
- 多普勒动态：0.020 Hz/s初始频漂、0.000020 Hz/s^2加加速度、0.5 Hz/120 s正弦扰动。

## 结果

| 用例 | 结论 | 频差 RMS | 频差 P95 | 码差 P95 | 最终/末段状态 |
|---|---|---:|---:|---:|---|
| [固定，40 dB-Hz](akf_fixed_strong_40_s20260715/result.md) | 通过 | 0.0089 Hz | 0.0176 Hz | 0.0037 chip | Strong |
| [自适应，40 dB-Hz](akf_adaptive_strong_40_s20260715/result.md) | 通过 | 0.0089 Hz | 0.0176 Hz | 0.0037 chip | Strong |
| [固定，40到7 dB-Hz](akf_fixed_40_to_7_s20260715/result.md) | 通过 | 1.5144 Hz | 2.1210 Hz | 0.1438 chip | Deep |
| [自适应，40到7 dB-Hz](akf_adaptive_40_to_7_s20260715/result.md) | 通过 | 1.5144 Hz | 2.1210 Hz | 0.1438 chip | Deep |
| [固定，40到3再到40 dB-Hz](akf_fixed_40_3_40_s20260715/result.md) | 通过 | 3.2503 Hz | 5.0735 Hz | 0.1014 chip | Deep/Weak/Medium/Strong |
| [自适应，40到3再到40 dB-Hz](akf_adaptive_40_3_40_s20260715/result.md) | 通过 | 2.9246 Hz | 4.8854 Hz | 0.1014 chip | Deep/Weak/Medium/Strong |

全部六组测试均无重新捕获、无状态切换后持续发散，帧有效率为100%。本轮为单种子
开发回归，不能表述为统计成功率。

## 跟踪图

| 模式 | 40 dB-Hz | 40到7 dB-Hz | 40到3再到40 dB-Hz |
|---|---|---|---|
| 固定 | [查看](akf_fixed_strong_40_s20260715/tracking.png) | [查看](akf_fixed_40_to_7_s20260715/tracking.png) | [查看](akf_fixed_40_3_40_s20260715/tracking.png) |
| 自适应 | [查看](akf_adaptive_strong_40_s20260715/tracking.png) | [查看](akf_adaptive_40_to_7_s20260715/tracking.png) | [查看](akf_adaptive_40_3_40_s20260715/tracking.png) |
