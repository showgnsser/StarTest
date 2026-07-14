# Slow deep fade and slow recovery

## Test scenario

A 120-second attenuation ramp models gradual obstruction, followed by a long weak hold and a 120-second recovery ramp.

- Duration: 480 s
- C/N0 mode: Linear
- C/N0 control points: [[0, 40], [60, 40], [180, 10], [300, 10], [420, 40], [480, 40]]

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
- Tail Doppler RMS / P95: 0.00614 / 0.01176 Hz
- Tail code phase MAE / P95: 0.00159 / 0.00336 chip
- C/N0 mean error / absolute P95: -0.734 / 2.671 dB
- Wall time: 52.05 s

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
| deep_fade | 200-300 | Weak | 1.09534 / 1.98474 | 0.05455 / 0.13070 | PASS |
| recovered | 440-480 | Track | 0.00614 / 0.01176 | 0.00159 / 0.00336 | PASS |

## Files

- `scenario.json`: published black-box input and expectation.
- `observations.csv`: sanitized 1 Hz observations.
- `state_events.csv`: public state and fault events.
- `tracking.png`: visual result.
