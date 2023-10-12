# coines_open_comm_intf
Opens the communication interface.
Currently only `COINES_COMM_INTF_USB` (USB Connection) interface is available.
`COINES_COMM_INTF_BLE` is available for `MCU_APP30` target.

In case of MCU Target, API waits indefinitely for serial port or BLE connection (`MCU_APP30` target only).

In order to use `fprintf` and `fscanf` with BLE, `intf_type` should be `COINES_COMM_INTF_BLE`


```C
int16_t coines_open_comm_intf(enum coines_comm_intf intf_type,void *arg); 
```