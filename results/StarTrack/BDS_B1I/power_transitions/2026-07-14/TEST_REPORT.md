# BDS B1I power-transition black-box test report

This report contains external scenarios, observations and acceptance results only.

| Case | Result | Final state | State commits | Doppler RMS (Hz) | Code P95 (chip) |
| --- | --- | --- | ---: | ---: | ---: |
| steady_strong_40 | PASS | Track | 3 | 0.04089 | 0.00355 |
| step_deep_fade | PASS | Track | 5 | 0.03858 | 0.00295 |
| slow_deep_fade | PASS | Track | 5 | 0.00614 | 0.00336 |
| short_shadow_5s | PASS | Track | 3 | 0.03198 | 0.00687 |
| threshold_ramp | PASS | Track | 5 | 0.03332 | 0.00404 |
| repeated_slow_fades | PASS | Track | 7 | 0.02780 | 0.00550 |
| slow_fade_drift_0p1 | PASS | Track | 5 | 0.03146 | 0.00279 |

## Conclusion

Passed cases satisfy their published black-box expectations. Failed cases are retained as regression evidence and must be re-run after the software fix.
