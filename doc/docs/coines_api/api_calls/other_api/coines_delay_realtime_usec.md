# coines_delay_realtime_usec
This API is used to introduce delay based on high precision RTC(LFCLK crystal) with the resolution of 30.517 usec.

```C
void coines_delay_realtime_usec(uint32_t period);
```

Arguments:

- `period`: required delay in microseconds. 