# coines_read_stream_sensor_data
Reads the data streamed from the sensor.

```C
int16_t coines_read_stream_sensor_data(uint8_t sensor_id, uint32_t number_of_samples, uint8_t *data, uint32_t *valid_samples_count);
```

Arguments:

- `sensor_id`: id of the sensor. 
- `number_of_samples`: number of samples the user wishes to read (not implemented).
- `data`: data buffer.
	- Interrupt streaming - Packet counter + Register data + Timestamp
	- Polling streaming - Register data.
- `valid_samples_count`: number of samples the user has actually received (may be less than `number_of_samples`).

Example of a packet:

<figure markdown>

  ![Image: Format of streaming packages](streaming_sample.png){ width="700"}
  <figcaption>Fig. 13: Format of streaming packages</figcaption>
</figure>

In the above figure, the following meaning apply to the mentioned abreviations:

- r~p~: Value at register address p.
- a: Size of register block–0.
- r~p+a~: Value at register address p.

Similarly is the case for r~q~, j and r~q+j~.
See the `coines_streaming_blocks` structure for information regarding register blocks.

The packet counter and the timestamp can be obtained as follows:

```C
packet_counter = (byte3_c << 24) | (byte2_c << 16) | (byte1_c << 8) | (byte0_c);
timestamp = (byte5_t << 40) | (byte4_t << 32) | (byte3_t << 24) | (byte2_t << 16) | (byte1_t << 8) | (byte0_t);
```

The 48-bit timestamp is enabled by using `coines_trigger_timer(COINES_TIMER_START,  COINES_TIMESTAMP_ENABLE);`

Timestamp in microseconds can be obtained using below formula:

$$ Timestamp\ (\mu s) = \frac{48bit\_timestamp}{30}$$