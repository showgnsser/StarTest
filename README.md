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

## 快速入口

- [全部测试用例矩阵](TEST_MATRIX.md)：按信号分组，逐用例列出输入、结果和详情链接。
- `results/`：每个用例的场景、公开观测、状态事件、图表和结果说明。
- `scenarios/`：可重复执行的黑盒测试集定义。

测试矩阵由以下命令重建：

```powershell
python tools\build_test_matrix.py
```

## 测试集分类

- `BDS_B1I/power_transitions`：短时功率变化与遮挡恢复测试。
- `BDS_B1I/realtime_tcxo_campaign`：15 个 900 s 实时 TCXO 等效动态测试，覆盖稳态灵敏度、极限边界、突变切换、缓慢衰减恢复和门限迟滞。
- `BDS_B1I/pll_pli_diagnostic`：强信号PLL参与度、PLI监测修正和强弱状态分工回归。
- `BDS_B1I/adaptive_kalman`：固定参数和受约束自适应模式的900 s黑盒A/B验证。
- `GPS_L1CA/cross_signal_regression`：L1CA强信号、24 dB-Hz牵引、短时强弱切换和900 s慢衰落边界。
- `GPS_L5/cross_signal_regression`：L5强信号、28 dB-Hz牵引、短时强弱切换和900 s慢衰落边界。
- `GPS_L1CA/state_sensitivity_matrix`、`GPS_L5/state_sensitivity_matrix`：固定状态灵敏度和自动强弱切换矩阵。
