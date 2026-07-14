# Five-second short obstruction

## Test scenario

A brief 10 dB-Hz shadow tests whether confirmation timers prevent unnecessary loss of synchronization or reacquisition.

- Duration: 150 s
- C/N0 mode: Step
- C/N0 control points: [[0, 40], [60, 10], [65, 40]]

## Expected result

- Acquire synchronization without reacquisition or transport faults.
- Finish in `Track`.
- Use at most 6 committed state changes.
- Tail Doppler RMS no greater than 5.000 Hz.
- Tail code phase P95 no greater than 0.150 chip.

## Actual result

- Overall: **PASS**
- Synchronization time: 1.22 s
- Final state: `Track`
- State path: ['Lock', 'Sync', 'Track']
- State commits: 3
- Tail Doppler RMS / P95: 0.03198 / 0.05090 Hz
- Tail code phase MAE / P95: 0.00248 / 0.00687 chip
- C/N0 mean error / absolute P95: 0.040 / 2.434 dB
- Wall time: 16.42 s

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
- window_short_shadow: PASS
- window_recovered: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| short_shadow | 60-65 | Track | 0.22333 / 0.38118 | 0.00711 / 0.01835 | PASS |
| recovered | 100-150 | Track | 0.03198 / 0.05090 | 0.00248 / 0.00687 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
