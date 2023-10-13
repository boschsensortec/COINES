# coinespy API calls: Sensor communication

For the definition of SPIBus, refer to [11.3.6.11](../definition_of_constants.md/#spibus). For the definition of I2CBus, refer to [11.3.6.10](../definition_of_constants.md/#i2cbus).
      
## config_i2c_bus
Configures the I~2~C bus

```python
coinesboard.config_i2c_bus(bus: I2CBus, i2c_address: int, i2c_mode: I2CMode) -> ErrorCodes
```

For the definition of I2CMode, refer to [11.3.6.4](../definition_of_constants.md/#i2cmode).

## config_spi_bus
Configures the SPI bus of the board.

```python
coinesboard.config_spi_bus(bus: SPIBus, cs_pin: MultiIOPin, spi_speed=SPISpeed,
spi_mode=SPIMode) -> ErrorCodes
```
For the definition of MultiIOPin, refer to [11.3.6.8](../definition_of_constants.md/#multiiopin). For the definition of SPISpeed, refer to [11.3.6.5](../definition_of_constants.md/#spispeed).
For the definition of SPIMode, refer to [11.3.6.7](../definition_of_constants.md/#spimode).

## deconfig_i2c_bus
This API is used to de-configure the I~2~C bus

```python
coinesboard.deconfig_i2c_bus(bus: I2CBus) -> ErrorCodes
```

## deconfig_spi_bus
This API is used to de-configure the SPI bus

```python
coinesboard.deconfig_spi_bus(bus: SPIBus) -> ErrorCodes
```

## write_i2c
Writes 8-bit register data to the I~2~C

```python
coinesboard.write_i2c(bus: I2CBus, register_address: int, register_value: int,
sensor_interface_detail: int = None) -> ErrorCodes
```
For the definition of parameters, refer to [6.6.7](../../../coines_api/api_calls/sensor_communication/coines_write_i2c.md).

## read_i2c
Reads 8-bit register data from the I~2~C

```python
register_data = coinesboard.read_i2c(bus: I2CBus, register_address: int, number_of_reads=1, sensor_interface_detail: int = None)
```
For the definition of parameters, refer to [6.6.8](../../../coines_api/api_calls/sensor_communication/coines_read_i2c.md).

## write_spi
Writes 8-bit register data to the SPI device.

```python
coinesboard.write_spi(bus: SPIBus, register_address: int, register_value: int,
sensor_interface_detail: int = None) -> ErrorCodes
```
For the definition of parameters, refer to [6.6.11](../../../coines_api/api_calls/sensor_communication/coines_write_spi.md).

## read_spi
Reads 8-bit register data from the SPI device.

```python
register_data = coinesboard.read_spi(bus: SPIBus, register_address: int,
number_of_reads=1, sensor_interface_detail: int = None)
```
For the definition of parameters, refer to [6.6.12](../../../coines_api/api_calls/sensor_communication/coines_read_spi.md).

## config_word_spi_bus
Configures the SPI bus parameters.

```python
coinesboard.config_word_spi_bus(bus: SPIBus, cs_pin: MultiIOPin,
spi_speed=SPISpeed.SPI_1_MHZ, spi_mode=SPIMode.MODE0,
spi_bits=SPITransferBits.SPI16BIT) -> ErrorCodes
```
For the definition of MultiIOPin, refer to [11.3.6.8](../definition_of_constants.md/#multiiopin). For the definition of SPISpeed, refer to [11.3.6.5](../definition_of_constants.md/#spispeed).
For the definition of SPITransferBits, refer to [11.3.6.6](../definition_of_constants.md/#spitransferbits).

## write_16bit_spi
Writes 16-bit register data to the SPI device.

```python
coinesboard.write_16bit_spi(bus: SPIBus, register_address: int, register_value:
List[int], sensor_interface_detail: int = None) -> ErrorCodes
```
For the definition of parameters, refer to [6.6.14](../../../coines_api/api_calls/sensor_communication/coines_write_16bit_spi.md).

## read_16bit_spi
Reads 16-bit register data from the SPI device.

```python
register_data = coinesboard.read_16bit_spi(bus: SPIBus, register_address: int,
number_of_reads=2, sensor_interface_detail: int = None)
```
For the definition of parameters, refer to [6.6.15](../../../coines_api/api_calls/sensor_communication/coines_read_16bit_spi.md).

## delay_milli_sec
Introduces delay in millisecond.

```python
coinesboard.delay_milli_sec(time_in_milli_sec=100)
```

## delay_micro_sec
Introduces delay in microsecond.

```python
coinesboard.delay_micro_sec(time_in_micro_sec=1)
```








