# coines_intf_available
Return the number of bytes available in the read buffer of the interface.
Works only on APP3.0 MCU target.

```C
uint16_t coines_intf_available(enum coines_comm_intf intf);
```

Arguments:

- `intf`: Type of interface (USB, COM, or BLE)
