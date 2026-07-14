# Slow deep fade with 0.1 Hz/s Doppler drift

## Test scenario

A gradual obstruction is combined with a continuous carrier drift to verify that stability gating preserves real dynamics.

- Duration: 360 s
- C/N0 mode: Linear
- C/N0 control points: [[0, 40], [60, 40], [150, 10], [240, 10], [330, 40], [360, 40]]

## Expected result

- Acquire synchronization without reacquisition or transport faults.
- Finish in `Track`.
- Use at most 8 committed state changes.
- Tail Doppler RMS no greater than 5.000 Hz.
- Tail code phase P95 no greater than 0.200 chip.

## Actual result

- Overall: **PASS**
- Synchronization time: 1.22 s
- Final state: `Track`
- State path: ['Lock', 'Sync', 'Track', 'Weak', 'Track']
- State commits: 5
- Tail Doppler RMS / P95: 0.03146 / 0.04102 Hz
- Tail code phase MAE / P95: 0.00138 / 0.00279 chip
- C/N0 mean error / absolute P95: -0.769 / 2.642 dB
- Wall time: 38.99 s

## Checks

- process_exit: PASS
- sync_acquired: PASS
- no_transport_fault: PASS
- no_reacquisition: PASS
- no_sync_loss_after_track: PASS
- final_state: PASS
- bounded_state_changes: PASS
- tail_doppler: PASS
- tail_code: PASS
- window_dynamic_fade: PASS
- window_dynamic_recovery: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| dynamic_fade | 180-240 | Weak | 2.10446 / 2.70982 | 0.07525 / 0.14133 | PASS |
| dynamic_recovery | 340-360 | Track | 0.03146 / 0.04102 | 0.00138 / 0.00279 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
