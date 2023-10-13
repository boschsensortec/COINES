# coines_i2c_set

This API is used to write the data in I2C communication.

```C
int8_t coines_i2c_set(enum coines_i2c_bus bus, uint8_t dev_addr, uint8_t *data, uint8_t count);
```

Arguments:

- bus: I2C bus to be used
- dev_addr: I2C device address.
- data: Data to be written.
- count: Number of bytes to write.