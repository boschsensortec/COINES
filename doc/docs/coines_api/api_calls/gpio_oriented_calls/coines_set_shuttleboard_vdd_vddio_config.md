# coines_set_shuttleboard_vdd_vddio_config
Configures the VDD and VDDIO of the sensor.
For APP2.0, a voltage level of 0 or 3300 mV is supported.
Any values above 0 will default to 3300 mV.

```C
int16_t coines_set_shuttleboard_vdd_vddio_config(uint16_t vdd_millivolt, uint16_t vddio_millivolt);
```