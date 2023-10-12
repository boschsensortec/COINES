# coines_write_spi
Writes 8-bit register data to the SPI device at `COINES_SPI_BUS_0`.

```C
int8_t coines_write_spi(enum coines_spi_bus bus,uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint16_t count);
```

Arguments:

- `bus`: SPI bus to be used.
- `dev_addr`: Chip select pin number.
- `reg_addr`: Starting address for writing the data.
- `reg_data`: Data to be written.
- `count`: Number of bytes to write.