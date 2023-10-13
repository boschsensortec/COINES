# coines_config_spi_bus
Configures the SPI bus of the board.
The argument coines_spi_bus refers to the bus on the board.
On APP2.0, there is only one bus available, so the user should only use `COINES_SPI_BUS_0`.
The SPI speed can be chosen in various discrete steps, as defined in enum coines_spi_speed in coines.h
(For example, `COINES_SPI_SPEED_2_MHZ` sets the SPI speed to 2 MHz).

```C
int16_t coines_config_spi_bus(enum coines_spi_bus bus, uint32_t spi_speed, enum coines_spi_mode spi_mode);
```