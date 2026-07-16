# Two repeated slow obstruction cycles

## Test scenario

Two deterministic attenuation and recovery cycles verify repeatability and absence of state chatter.

- Duration: 450 s
- C/N0 mode: Linear
- C/N0 control points: [[0, 40], [60, 40], [120, 12], [150, 12], [210, 40], [240, 40], [300, 12], [330, 12], [390, 40], [450, 40]]

## Expected result

- Acquire synchronization without reacquisition or transport faults.
- Finish in `Track`.
- Use at most 12 committed state changes.
- Tail Doppler RMS no greater than 5.000 Hz.
- Tail code phase P95 no greater than 0.150 chip.

## Actual result

- Overall: **PASS**
- Synchronization time: 1.22 s
- Final state: `Track`
- State path: ['Lock', 'Sync', 'Track', 'Weak', 'Track', 'Weak', 'Track']
- State commits: 7
- Tail Doppler RMS / P95: 0.02780 / 0.05257 Hz
- Tail code phase MAE / P95: 0.00266 / 0.00550 chip
- C/N0 mean error / absolute P95: -0.844 / 4.170 dB
- Wall time: 49.86 s

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
- window_first_fade: PASS
- window_second_fade: PASS
- window_recovered: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| first_fade | 125-150 | Weak | 0.72319 / 0.84150 | 0.11327 / 0.14399 | PASS |
| second_fade | 305-330 | Weak | 0.28675 / 0.32360 | 0.07094 / 0.09597 | PASS |
| recovered | 410-450 | Track | 0.02780 / 0.05257 | 0.00266 / 0.00550 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
