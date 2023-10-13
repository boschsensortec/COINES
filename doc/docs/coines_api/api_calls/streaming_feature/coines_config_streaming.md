# coines_config_streaming
Sets the configuration for streaming sensor data.

```C
int16_t coines_config_streaming(uint8_t channel_id, struct coines_streaming_config *stream_config, struct coines_streaming_blocks *data_blocks); 
```

Arguments:

- `channel_id`: An integer number that can be used as identifier/index to the sensor data that will be streamed for this setting.
- `stream_config`: Contains information regarding interface settings and streaming configuration.
-  `coines_streaming_blocks`: Contains information regarding numbers of register blocks, range and size of  each block.

**Note**:

The below parameters should always be set:

- `data_block.no_of_blocks`: number of blocks to stream (must at least be one).
- For each block b:
	- `data_block.reg_start_addr[b]`: start address of the block in the register map.
	- `stream_block.no_of_data_bytes[b]`: number of addresses to read, starting from the start address.

For reading data from I~2~C bus,then set the below parameters:
	
- `stream_config.intf = COINES_SENSOR_INTF_I2C;`
- `stream_config.i2c_bus`: I~2~C bus (in case of APP2.0, this is always `COINES_I2C_BUS_0`).
- `stream_config.dev_addr`: I~2~C address of the sensor.

For reading data from SPI bus, then set the below parameters:

- `stream_config.intf = COINES_SENSOR_INTF_SPI;`
- `stream_config.spi_bus`: SPI bus (in case of APP2.0, this is always `COINES_SPI_BUS_0`).
- `stream_config.cs_pin`: CS pin of the sensor, information can be obtained from the shuttle board documentation for the sensor. 

When polling mode is requested, set the below parameters:

- `stream_config.sampling_units`:  
either in milliseconds (`COINES_SAMPLING_TIME_IN_MILLI_SEC`)  
or in microseconds (`COINES_SAMPLING_TIME_IN_MICRO_SEC`)

- `stream_config.sampling_time`: sampling period is in the unit as defined in `stream_config.sampling_units`.

When interrupt mode is requested, set the below parameters:

- `stream_config.int_pin`: Pin of the interrupt which shall trigger the sensor read-out. If the interrupt output of the sensor is used, the required information about the pin number can be obtained from the shuttle board documentation for the sensor.
- `stream_config.int_timestamp`:  It can be configured if the sensor data is tagged with a timestamp (`COINES_TIMESTAMP_ENABLE`) or not (`COINES_TIMESTAMP_DISABLE`).