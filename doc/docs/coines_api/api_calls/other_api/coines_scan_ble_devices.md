# coines_scan_ble_devices
This API is used to connect to BLE Adapter and return list of BLE peripherals found during BLE scan.
```C
int8_t coines_scan_ble_devices(struct ble_peripheral_info *ble_info, uint8_t
*peripheral_count, size_t scan_timeout_ms)
```

Arguments:

- `ble_info` :  array of struct containing found BLE peripheral information.
  
- `peripheral_count` :  number of BLE peripherals found.

- `scan_timeout_ms` : timeout for BLE scan.



