# coines_set_led
 This API is used to set led state(on or off).
 
```C
int16_t coines_set_led(enum coines_led led,enum coines_led_state led_state);
```

Arguments:

- `led`: led whose state has to be set.
- `led_state`: state to be set to the given led.