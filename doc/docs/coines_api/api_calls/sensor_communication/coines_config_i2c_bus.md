# coines_config_i2c_bus
Configures the I~2~C bus. 

```C
int16_t coines_config_i2c_bus(enum coines_i2c_bus bus, enum coines_i2c_mode i2c_mode);
```

The first argument refers to the bus on the board.
Currently, on APP2.0, there is only one bus available, so the argument is always `COINES_I2C_BUS_0`.

The following I~2~C modes are available:
```C
COINES_I2C_STANDARD_MODE
COINES_I2C_FAST_MODE
COINES_I2C_SPEED_3_4_MHZ
COINES_I2C_SPEED_1_7_MHZ
```