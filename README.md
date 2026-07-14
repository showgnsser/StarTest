# StarTest

StarTest 保存 Star 系列 GNSS 软件的黑盒测试结果。

仓库只记录以下内容：

- 测试场景与外部输入；
- 可公开的输出观测；
- 预期结果与验收门限；
- 实际结果、图表和通过结论。

仓库不保存鉴别器公式、环路滤波器参数、状态判据实现、相关器内部量或其他算法细节。
这些内容分别保存在 StarTrack 和 StarGen 软件仓库中。

## 目录

```text
scenarios/StarTrack/<signal>/<category>/  黑盒场景清单
results/StarTrack/<signal>/<category>/    按日期归档的结果
docs/                                     测试发布规范
```

首个测试集为 BDS B1I 的功率变化与遮挡恢复测试。
