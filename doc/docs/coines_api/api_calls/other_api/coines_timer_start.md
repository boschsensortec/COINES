# coines_timer_start
This API is used to start the configured hardware timer.
 
```C
int16_t coines_timer_start(enum coines_timer_instance instance, uint32_t timeout);
```

Arguments:

- `instance`: timer instance.
- `timeout`: timeout in microseconds.