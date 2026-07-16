# 40 dB-Hz strong-signal baseline

## Test scenario

A stable open-sky signal verifies acquisition handoff and the normal steady state before fade testing.

- Duration: 90 s
- C/N0 mode: Step
- C/N0 control points: [[0, 40]]

## Expected result

- Acquire synchronization without reacquisition or transport faults.
- Finish in `Track`.
- Use at most 4 committed state changes.
- Tail Doppler RMS no greater than 5.000 Hz.
- Tail code phase P95 no greater than 0.100 chip.

## Actual result

- Overall: **PASS**
- Synchronization time: 1.22 s
- Final state: `Track`
- State path: ['Lock', 'Sync', 'Track']
- State commits: 3
- Tail Doppler RMS / P95: 0.04089 / 0.07065 Hz
- Tail code phase MAE / P95: 0.00161 / 0.00355 chip
- C/N0 mean error / absolute P95: -0.526 / 1.016 dB
- Wall time: 10.11 s

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
- window_strong_hold: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| strong_hold | 60-90 | Track | 0.04089 / 0.07065 | 0.00161 / 0.00355 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
