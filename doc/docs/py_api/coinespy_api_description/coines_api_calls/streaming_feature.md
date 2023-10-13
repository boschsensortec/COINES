# coinespy API calls: Streaming feature

## config_streaming
Sets the configuration for streaming sensor data.

```python
coinesboard.config_streaming(sensor_id: int,
stream_config: StreamingConfig, data_blocks: StreamingBlocks) -> ErrorCodes
```

Arguments:

- `sensor_id` : An integer number that can be used as identifier/index to the sensor data that will
be streamed for this setting.  
- `stream_config` : Contains information regarding interface settings and streaming configuration.
- `data_blocks` : Contains information regarding numbers of blocks to read, register address and
size for each block.

**Note:**

The below parameters should always be set:

- `data_blocks.NoOfBlocks` :  number of blocks to stream (must at least be one).
- For each block b:
  - `data_blocks.RegStartAddr[b]` : start address of the block in the register map
  - `data_blocks.NoOfDataBytes[b]` :  number of bytes to read, starting from the start address

For reading data from I~2~C bus,then set the below parameters:

- `stream_config.Intf` = `cpy.SensorInterface.I2C.value`
- `stream_config.I2CBus` : I2C bus (in case of APP2.0 and APP3.0, this is always
`cpy.I2CBus.BUS_I2C_0.value`)
- `stream_config.DevAddr` : I2C address of the sensor

For reading data from SPI bus, then set the below parameters:

- `stream_config.Intf` = ` cpy.SensorInterface.SPI.value`;
- `stream_config.SPIBus` : SPI bus (in case of APP2.0 and APP3.0, this is always
`cpy.SPIBus.BUS_SPI_0.value`)
- `stream_config.CSPin` : CS pin of the sensor, information can be obtained from the shuttle
board documentation for the sensor.
- `stream_config.SPIType`: 0 : 8-bit SPI; 1 : 16-bit SPI

When polling mode is requested, set the below parameters:

- `stream_config.SamplingUnits` : either milliseconds or microseconds. Refer to [11.3.6.15](../definition_of_constants.md/#samplingunits).
- `stream_config.SamplingTime` : Sampling period in the unit as defined in
`stream_config.SamplingUnits`.

When interrupt mode is requested, set the below parameters:

- ``stream_config.IntPin`` : pin of the interrupt which shall trigger the sensor read-out. If the
interrupt output of the sensor is used, the required information about the pin number can be
obtained from the shuttle board documentation for the sensor.
- ``stream_config.IntTimeStamp``: it can be configured if the sensor data is tagged with a timestamp - 1 or not - 0.
- `stream_config.HwPinState`: State of the hardware pin connected to the interrupt line - 0/1 : Low/high

Below parameters are common for both streaming types:

- ``stream_config.IntlineCount`` : Number of interrupt lines to be used for monitoring interrupts.
- ``stream_config.IntlineInfo`` : List of pin numbers that correspond to interrupt lines being used
for interrupt monitoring.
- ``stream_config.ClearOnWrite`` : 0/1 : Disable/enable "clear on write" feature.

The below parameters should be set only when stream_config.ClearOnWrite = 1:

- ``stream_config.ClearOnWriteConfig.StartAddress``: Address of the sensor register at which
the process of clearOnWrite should initiate.
- ``stream_config.ClearOnWriteConfig.DummyByte``: Number of padding bytes that must be added before clearing the bytes starting from the designated address.
- ``stream_config.ClearOnWriteConfig.NumBytesToClear``: Number of bytes that need to be cleared.

Below is the Python code snippet for interrupt streaming

```python
# Store streaming settings in local variables
accel_stream_settings = dict(
  I2C_ADDR_PRIMARY=0x18,
  NO_OF_BLOCKS = 2,
  REG_X_LSB= [0x12, 0x00],
  NO_OF_DATA_BYTES= [6, 1],
  CHANNEL_ID=1,
  CS_PIN=cpy.MultiIOPin.SHUTTLE_PIN_8.value,
  INT_PIN=cpy.MultiIOPin.SHUTTLE_PIN_21.value,
  INT_TIME_STAMP=1,
)

gyro_stream_settings = dict(
  I2C_ADDR_PRIMARY=0x68,
  NO_OF_BLOCKS = 2,
  REG_X_LSB= [0x02,0x00],
  NO_OF_DATA_BYTES = [6, 1],
  CHANNEL_ID=2,
  CS_PIN=cpy.MultiIOPin.SHUTTLE_PIN_14.value,
  INT_PIN=cpy.MultiIOPin.SHUTTLE_PIN_22.value,
  INT_TIME_STAMP=1,
)

# set the config_streaming parameters
stream_config = cpy.StreamingConfig()
data_blocks = cpy.StreamingBlocks()
if self.interface == cpy.SensorInterface.I2C:
  stream_config.Intf = cpy.SensorInterface.I2C.value
  stream_config.I2CBus = cpy.I2CBus.BUS_I2C_0.value
  stream_config.DevAddr = sensor["I2C_ADDR_PRIMARY"]

elif self.interface == cpy.SensorInterface.SPI:
  stream_config.Intf = cpy.SensorInterface.SPI.value
  stream_config.SPIBus = cpy.SPIBus.BUS_SPI_0.value
  stream_config.CSPin = sensor["CS_PIN"]

if sensor_type == bmi08x.SensorType.ACCEL and self.interface == cpy.SensorInterface.SPI:
  # extra dummy byte for SPI
  dummy_byte_offset = 1
else:
  dummy_byte_offset = 0

data_blocks.NoOfBlocks = sensor["NO_OF_BLOCKS"]
for i in range(0, data_blocks.NoOfBlocks):
  data_blocks.RegStartAddr[i] = sensor["REG_X_LSB"][i]
  data_blocks.NoOfDataBytes[i] = sensor["NO_OF_DATA_BYTES"][i] + dummy_byte_offset

stream_config.IntTimeStamp = sensor["INT_TIME_STAMP"]
stream_config.IntPin = sensor["INT_PIN"]

# call config_streaming API for each sensor to configure the streaming settings
ret = coinesboard.config_streaming(
  accel_sensor_id, self.accel_stream_config, self.accel_data_blocks)
ret = coinesboard.config_streaming(
  gyro_sensor_id, self.accel_stream_config, self.accel_data_blocks)
```
## start_stop_streaming

Starts or stops sensor data streaming.
```python
coinesboard.start_stop_streaming(stream_mode: StreamingMode, start_stop:
  StreamingState) -> ErrorCodes
```
For the definition of StreamingMode, refer to [11.3.6.13](../definition_of_constants.md/#streamingmode). For the definition of StreamingState, refer to [11.3.6.14](../definition_of_constants.md/#streamingstate).

## read_stream_sensor_data

Reads the data streamed from the sensor.
```python
coinesboard.read_stream_sensor_data(sensor_id: int, number_of_samples: int, buffer_size=STREAM_RSP_BUF_SIZE) -> Tuple[ErrorCodes, list, int]
```
Return:

Tuple of ErrorCodes, data and valid_samples_count
For the detailed definition of parameters, refer to [6.7.3](../../../coines_api/api_calls/streaming_feature/coines_read_stream_sensor_data.md).



 