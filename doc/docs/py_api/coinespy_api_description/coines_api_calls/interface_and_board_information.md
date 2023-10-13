# coinespy API calls: Interface and board information

## open_comm_interface
Sets the communication interface between board and PC to USB or Serial.

```python
coinesboard.open_comm_interface(interface=CommInterface.USB, arg=None) -> ErrorCodes
```

For the definition of CommInterface, refer to [11.3.6.3](../definition_of_constants.md/#comminterface).

## close_comm_interface
Disposes the resources used by the USB/serial/BLE communication.

```python
coinesboard.close_comm_interface(arg=None) -> ErrorCodes
```

## get_board_info
Obtains board specific information.

```python
BoardInfo = coinesboard.get_board_info()
# Return:
BoardInfo.HardwareId # Hardware ID
BoardInfo.SoftwareId # Firmware version information
BoardInfo.Board # Board type
BoardInfo.ShuttleID # ID of shuttle, in case a shuttle is detected
```

## scan_ble_devices
This API is used to connect to BLE Adapter and return list of BLE peripherals found during BLE
scan.

```python
ble_info, peripheral_count = coinesboard.scan_ble_devices(scan_timeout_ms=0) -> Tuple[list, int]
```
For the definition of parameters, refer to [6.8.29](../../../coines_api/api_calls/other_api/coines_scan_ble_devices.md).

## echo_test
This API is used to test the communication.

```python
coinesboard.echo_test(data: List[int]) -> ErrorCodes
```
Arguments:

- `data`: Data to be sent for testing.
 