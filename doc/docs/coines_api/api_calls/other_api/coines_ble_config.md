# coines_ble_config
This API is used to configure BLE name and power. It should be called before calling coines_open_comm_intf API.

```C
int16_t coines_ble_config(struct coines_ble_config *ble_config);
```

Arguments:

- `ble_config`: structure holding ble name and power details.