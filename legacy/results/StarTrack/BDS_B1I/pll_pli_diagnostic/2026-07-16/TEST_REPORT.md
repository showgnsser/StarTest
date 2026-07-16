# BDS B1I PLL and PLI black-box diagnostic

## Background

The previous realtime campaign showed a low PLI during strong-signal tracking. This diagnostic separates the carrier-quality monitor from actual PLL participation and republishes two 900 s realtime runs.

## Results

| Case | Result | State path | Doppler RMS / P95 (Hz) | Code P95 (chip) |
| --- | --- | --- | ---: | ---: |
| steady_40_seed20260716 | PASS | PullIn -> Lock -> Strong | 0.225 / 0.478 | 0.003 |
| transition_40_24_16_12_7_16_40_seed20260716 | PASS | PullIn -> Lock -> Strong -> LongFast -> LongLock -> Medium -> Weak -> Deep -> Weak -> Medium -> Strong | 0.250 / 0.580 | 0.028 |


## Conclusion

- The steady 40 dB-Hz run confirms continuous PLL participation and a high, stable PLI after acquisition handoff.
- The transition run confirms PLL participation in strong and medium states and PLL shutdown in weak and deep states.
- Neither run reacquired or diverged after a state transition.
- The old PLI values are superseded for lock-quality interpretation; frequency, code phase and state-transition results remain valid.
