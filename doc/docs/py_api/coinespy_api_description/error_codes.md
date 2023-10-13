# Error Codes
Error codes are not (always) returned by the different function calls. Internally, an error_code variable is maintained which is updated after the function call. It can be read out and checked by the user afterwards. 

Example:

```python
import coinespy as cpy
board = cpy.CoinesBoard()
try:
    board.open_comm_interface(cpy.CommInterface.USB)
    board.close_comm_interface()
except:
    print(f’Could not connect to board: {board.error_code}’)
    exit(board.error_code)
```

## General Error Codes
Error code definitions
```python
class ErrorCodes(Enum):
    COINES_SUCCESS = 0
    COINES_E_FAILURE = -1
    COINES_E_COMM_IO_ERROR = -2
    COINES_E_COMM_INIT_FAILED = -3
    COINES_E_UNABLE_OPEN_DEVICE = -4
    COINES_E_DEVICE_NOT_FOUND = -5
    COINES_E_UNABLE_CLAIM_INTERFACE = -6
    COINES_E_MEMORY_ALLOCATION = -7
    COINES_E_NOT_SUPPORTED = -8
    COINES_E_NULL_PTR = -9
    COINES_E_COMM_WRONG_RESPONSE = -10
    COINES_E_SPI16BIT_NOT_CONFIGURED = -11
    COINES_E_SPI_INVALID_BUS_INTERFACE = -12
    COINES_E_SPI_CONFIG_EXIST = -13
    COINES_E_SPI_BUS_NOT_ENABLED = -14
    COINES_E_SPI_CONFIG_FAILED = -15
    COINES_E_I2C_INVALID_BUS_INTERFACE = -16
    COINES_E_I2C_BUS_NOT_ENABLED = -17
    COINES_E_I2C_CONFIG_FAILED = -18
    COINES_E_I2C_CONFIG_EXIST = -19
    COINES_E_TIMER_INIT_FAILED = -20
    COINES_E_TIMER_INVALID_INSTANCE = -21
    COINES_E_TIMER_CC_CHANNEL_NOT_AVAILABLE = -22
    COINES_E_EEPROM_RESET_FAILED = -23
    COINES_E_EEPROM_READ_FAILED = -24
    COINES_E_INIT_FAILED = -25
    COINES_E_STREAM_NOT_CONFIGURED = -26
    COINES_E_STREAM_INVALID_BLOCK_SIZE = -27
    COINES_E_STREAM_SENSOR_ALREADY_CONFIGURED = -28
    COINES_E_STREAM_CONFIG_MEMORY_FULL = -29
    COINES_E_INVALID_PAYLOAD_LEN = -30
    COINES_E_CHANNEL_ALLOCATION_FAILED = -31
    COINES_E_CHANNEL_DE_ALLOCATION_FAILED = -32
    COINES_E_CHANNEL_ASSIGN_FAILED = -33
    COINES_E_CHANNEL_ENABLE_FAILED = -34
    COINES_E_CHANNEL_DISABLE_FAILED = -35
    COINES_E_INVALID_PIN_NUMBER = -36
    COINES_E_MAX_SENSOR_COUNT_REACHED = -37
    COINES_E_EEPROM_WRITE_FAILED = -38
    COINES_E_INVALID_EEPROM_RW_LENGTH = -39
```