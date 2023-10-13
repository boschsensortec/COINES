# coines_trigger_timer
Triggers the timer in firmware and also enables or disables the time stamp feature.

```C
int16_t coines_trigger_timer(enum coines_timer_config tmr_cfg,enum coines_time_stamp_config ts_cfg);
```

Arguments:

- `tmr_cfg`: start, stop or reset the timer (`COINES_TIMER_START`, `COINES_TIMER_STOP` or `COINES_TIMER_RESET`). 
- `ts_cfg`: Enables/disables microcontroller timestamp  (`COINES_TIMESTAMP_ENABLE` or `COINES_TIMESTAMP_DISABLE`).