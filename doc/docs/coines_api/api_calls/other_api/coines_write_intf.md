# coines_write_intf
Write data over the specified interface.Works only on APP3.0 MCU target.

```C
uint16_t coines_write_intf(enum coines_comm_intf intf, void *buffer, uint16_t len);
```

Arguments:

- `intf`: Type of interface (USB, COM, or BLE)
- `buffer`: Pointer to the buffer storing the data
- `len`: Length of the buffer
