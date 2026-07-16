# Slow variation around the weak-signal boundary

## Test scenario

The signal slowly crosses the weak-signal region and then recovers, exercising state hysteresis without rapid power steps.

- Duration: 480 s
- C/N0 mode: Linear
- C/N0 control points: [[0, 40], [60, 40], [150, 17], [210, 17], [300, 23], [360, 23], [420, 40], [480, 40]]

## Expected result

- Acquire synchronization without reacquisition or transport faults.
- Finish in `Track`.
- Use at most 8 committed state changes.
- Tail Doppler RMS no greater than 5.000 Hz.
- Tail code phase P95 no greater than 0.150 chip.

## Actual result

- Overall: **PASS**
- Synchronization time: 1.22 s
- Final state: `Track`
- State path: ['Lock', 'Sync', 'Track', 'Weak', 'Track']
- State commits: 5
- Tail Doppler RMS / P95: 0.03332 / 0.05952 Hz
- Tail code phase MAE / P95: 0.00192 / 0.00404 chip
- C/N0 mean error / absolute P95: -0.675 / 1.464 dB
- Wall time: 52.03 s

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
- window_boundary_hold: PASS
- window_recovered: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| boundary_hold | 170-280 | Weak | 0.37663 / 0.56886 | 0.01431 / 0.02941 | PASS |
| recovered | 440-480 | Track | 0.03332 / 0.05952 | 0.00192 / 0.00404 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
