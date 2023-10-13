# coines_read_i2c
Reads 8-bit register data from the I~2~C device at `COINES_I2C_BUS_0`.

```C
int8_t coines_read_i2c(enum coines_i2c_bus bus,uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint16_t count);
```

Arguments:

- `bus`: I~2~C bus to be used.
- `dev_addr`: I~2~C device address.
- `reg_addr`: Starting address for reading the data.
- `reg_data`: Buffer to take up the read data.
- `count`: Number of bytes to read.