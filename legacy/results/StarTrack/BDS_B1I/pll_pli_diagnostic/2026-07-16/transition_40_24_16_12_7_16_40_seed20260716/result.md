# PLL participation across strong-to-deep transitions

## 测试场景

Verify PLL participation in strong and medium states, PLL shutdown in weak states, and stable recovery.

- 时长：900 s
- 种子：20260716
- TCXO等效动态：0.020 Hz/s线性频漂，叠加0.50 Hz、120 s周期慢变化
- C/N0时间表：[{'time_s': 0.0, 'cn0_db_hz': 40.0}, {'time_s': 120.0, 'cn0_db_hz': 24.0}, {'time_s': 240.0, 'cn0_db_hz': 16.0}, {'time_s': 360.0, 'cn0_db_hz': 12.0}, {'time_s': 480.0, 'cn0_db_hz': 7.0}, {'time_s': 660.0, 'cn0_db_hz': 16.0}, {'time_s': 780.0, 'cn0_db_hz': 40.0}]

## 预期结果

- 无重新捕获和状态切换后发散。
- 末段多普勒P95不超过5 Hz。
- 末段码相位P95不超过0.2 chip。
- PLL参与度与当前状态配置一致。

## 实际结果

- 结果：**PASS**
- 状态路径：`PullIn -> Lock -> Strong -> LongFast -> LongLock -> Medium -> Weak -> Deep -> Weak -> Medium -> Strong`
- 末段多普勒RMS / P95：0.2501 / 0.5799 Hz
- 末段码相位P95：0.0280 chip
- 回捕次数：0
- 切换后发散次数：0

## 文件

- `observations.csv`：1 Hz状态、PLI、PLL启用标志、PLL控制贡献和跟踪真值误差。
- `state_events.csv`：状态与同步事件。
- `tracking.png`：PLL启用、PLI、C/N0及跟踪误差图。
