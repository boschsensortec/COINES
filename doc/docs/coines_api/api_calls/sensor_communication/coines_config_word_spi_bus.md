# coines_config_word_spi_bus
Configures the SPI bus parameters speed, mode, 8-bit/16-bit transfer ( `COINES_SPI_TRANSFER_8BIT` / `COINES_SPI_TRANSFER_16BIT` ).

```C
int16_t coines_config_word_spi_bus(enum coines_spi_bus bus, enum coines_spi_speed spi_speed, enum coines_spi_mode spi_mode, enum coines_spi_transfer_bits spi_transfer_bits);
```