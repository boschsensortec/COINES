# coines_timer_config
 This API is used to configure the hardware timer.
 
```C
int16_t coines_timer_config(enum coines_timer_instance instance, void* handler);
```

Arguments:

- `instance`: timer instance.
- `handler`: callback to be called when timer expires.
