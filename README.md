# StarTest

StarTest 是 Star 系列 GNSS 软件的固定黑盒 Qualification 基准库。主目录
按“软件 -> 信号 -> 固定现实场景”组织，运行日期只保存在结果元数据中，
不再复制目录或改变案例 ID。

仓库公开信号真值、外部输入、验收门限、1 Hz 输出、图表和结论；鉴别器
公式、滤波器参数及其他算法实现仍只保存在对应软件仓库。

## 快速入口

- [固定测试矩阵](TEST_MATRIX.md)
- [GPS L1CA](StarTrack/GPS_L1CA/README.md)
- [BDS B1I](StarTrack/BDS_B1I/README.md)
- [GPS L5](StarTrack/GPS_L5/README.md)
- [发布规范](docs/test_policy.md)
- [旧日期归档](legacy/README.md)

## 固定结构

```text
StarTrack/
  GPS_L1CA/
    README.md
    01_pull_in_sensitivity/
      README.md
      scenario.json
      runs/
        startrack-<commit>_<profile-version>/
          summary.json
          metrics.csv
          seed-001/
            observations.csv
            state_events.csv
          figures/
  BDS_B1I/
  GPS_L5/
legacy/
```

每个信号固定回答三个问题：牵引灵敏度、无电文辅助持续灵敏度、已知
电文辅助持续灵敏度。随后用多普勒动态、强弱阶跃、缓慢遮挡、门限徘徊
和耐久场景检验这些指标能否在真实时钟扰动下稳定保持。

## 两套测试

- `Development`：定义保存在 StarTrack，默认单种子和短时运行，结果只留
  本地，用于日常调试。
- `Qualification`：定义与公开结果保存在本仓库，常规场景3个固定种子，
  灵敏度边界5个固定种子。

5种子结果用于工程基准，不表述为统计意义上的95%成功概率。

## 工具

```powershell
python tools\validate_catalog.py
python tools\build_test_matrix.py
```

`validate_catalog.py` 检查固定案例 ID、必需报告章节、物理单位、Git版本、
种子完整性和图片链接。失败用例不会删除，它是后续算法版本必须保留的
回归边界。
