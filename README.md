# StarTest

StarTest 保存 Star 系列 GNSS 软件的黑盒测试结果。

仓库记录以下内容：

- 测试场景、信号真值和外部输入；
- 可公开的跟踪输出观测；
- 预期结果、验收门限和实际结论；
- 状态变化、精度统计和可视化图表。

仓库不保存鉴别器公式、环路滤波器参数、内部状态判据、相关器内部量或其他算法实现细节。这些内容分别保存在 StarTrack 和 StarGen 软件仓库中。

## 目录

```text
scenarios/StarTrack/<signal>/<category>/  黑盒场景清单
results/StarTrack/<signal>/<category>/    按日期归档的结果
docs/                                     测试发布规范
```

## 已发布测试集

- `GPS_L1CA/state_sensitivity_matrix`：九状态固定灵敏度、阶梯、缓慢衰落、短遮挡和无辅助弱信号对照，共21个开发用例。
- `GPS_L5/state_sensitivity_matrix`：导频九状态固定灵敏度、阶梯、缓慢衰落和短遮挡，共15个开发用例。
- `BDS_B1I/power_transitions`：短时功率变化与遮挡恢复测试。
- `BDS_B1I/realtime_tcxo_campaign`：15 个 900 s 实时 TCXO 等效动态测试，覆盖稳态灵敏度、极限边界、突变切换、缓慢衰减恢复和门限迟滞。
- `BDS_B1I/pll_pli_diagnostic`：强信号PLL参与度、PLI监测修正和强弱状态分工回归。
- `GPS_L1CA/cross_signal_regression`：L1CA强信号、24 dB-Hz牵引、短时强弱切换和900 s慢衰落边界。
- `GPS_L5/cross_signal_regression`：L5强信号、28 dB-Hz牵引、短时强弱切换和900 s慢衰落边界。
