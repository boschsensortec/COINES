# coines_flush_intf
Flush the write buffer.Works only on APP3.0 MCU target.

```C
void coines_flush_intf(enum coines_comm_intf intf);
```

Arguments:

- `intf`: Type of interface (USB, COM, or BLE)
