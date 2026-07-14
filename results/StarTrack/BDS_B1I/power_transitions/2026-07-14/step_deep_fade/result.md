# Abrupt deep fade and recovery

## Test scenario

The signal drops from 40 to 10 dB-Hz, remains obstructed, and returns abruptly to 40 dB-Hz.

- Duration: 220 s
- C/N0 mode: Step
- C/N0 control points: [[0, 40], [60, 10], [140, 40]]

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
- Tail Doppler RMS / P95: 0.03858 / 0.08081 Hz
- Tail code phase MAE / P95: 0.00121 / 0.00295 chip
- C/N0 mean error / absolute P95: -0.268 / 8.442 dB
- Wall time: 24.32 s

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
- window_deep_fade: PASS
- window_recovered: PASS

## Interval results

| Window | Time (s) | States | Doppler RMS / P95 (Hz) | Code MAE / P95 (chip) | Result |
| --- | --- | --- | ---: | ---: | --- |
| deep_fade | 80-130 | Weak | 1.73004 / 2.37389 | 0.05677 / 0.08923 | PASS |
| recovered | 180-220 | Track | 0.03858 / 0.08081 | 0.00121 / 0.00295 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
