# coines_read_bat_status
This API is used to read the battery status.

```C
int16_t coines_read_bat_status(uint16_t *bat_status_mv, uint8_t *bat_status_percent);
```

Arguments:

- `bat_status_mv`: Buffer to retrieve the battery status in millivolt.
- `bat_status_percent`: Buffer to retrieve the battery status in percentage.