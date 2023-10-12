# coines_start_stop_streaming
Starts or stops sensor data streaming.

```C
int16_t coines_start_stop_streaming(enum coines_streaming_mode stream_mode, uint8_t start_stop);
```

Arguments:

- `stream_mode`: streaming mode (either `COINES_STREAMING_MODE_POLLING` or  
`COINES_STREAMING_MODE_INTERRUPT`).
- `start_stop`: flag to either start (`COINES_STREAMING_START`) or stop (`COINES_STREAMING_STOP`) the streaming.