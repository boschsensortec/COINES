# coines_intf_connected
Check if the interface is connected.Works only on APP3.0 MCU target.

```C
bool coines_intf_connected(enum coines_comm_intf intf);
```

Arguments:

- `intf`: Type of interface (USB, COM, or BLE)