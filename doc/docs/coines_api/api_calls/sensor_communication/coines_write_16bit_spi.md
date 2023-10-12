# coines_write_16bit_spi
Writes 16-bit register data to the SPI device at `COINES_SPI_BUS_0`.

```C
int8_t coines_write_16bit_spi(enum coines_spi_bus bus, uint8_t cs, uint16_t reg_addr, void *reg_data, uint16_t count);
```

Arguments:

- `bus`: SPI bus to be used.
- `cs`: Chip select pin number.
- `reg_addr`: Starting address for writing the data.
- `reg_data`: Data to be written.
- `count`: Number of bytes to write.