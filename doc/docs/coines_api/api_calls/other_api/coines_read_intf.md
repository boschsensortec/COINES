# coines_read_intf
Read data over the specified interface.Works only on APP3.0 MCU target.

```C
uint16_t coines_read_intf(enum coines_comm_intf intf, void *buffer, uint16_t len);
```

Arguments:

- `intf`: Type of interface (USB, COM, or BLE)
- `buffer`: Pointer to the buffer to store the data
- `len`: Length of the buffer