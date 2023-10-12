# coines_read_16bit_spi
Reads 16-bit register data from the SPI device at `COINES_SPI_BUS_0`.

```C
int8_t coines_read_16bit_spi(enum coines_spi_bus bus, uint8_t cs, uint16_t reg_addr, void *reg_data, uint16_t count);
```

Arguments:

- `bus`: SPI bus to be used.
- `cs`: Chip select pin number.
- `reg_addr`: Starting address for reading the data.
- `reg_data`: Buffer to take up the read data.
- `count`: Number of bytes to read.