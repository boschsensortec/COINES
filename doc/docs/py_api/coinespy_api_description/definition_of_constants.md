#  Definiton of constants

## PinDirection
Pin mode definitions.
```python
class PinDirection:
    INPUT = 0 # COINES_PIN_DIRECTION_IN = 0
    OUTPUT = 1
```

## PinValue
Pin level definitions.
```python
class PinValue:
    LOW = 0 # COINES_PIN_VALUE_LOW = 0
    HIGH = 1
```

## CommInterface
Definition of Communication interface.
```python
class CommInterface:
    USB = 0
    SERIAL = 1
    BLE = 2
```

## I2CMode
Definition of the speed of I2C bus.
```python
class I2CMode:
    STANDARD_MODE = 0 # Standard mode - 100kHz
    FAST_MODE = 1 # Fast mode - 400kHz
    SPEED_3_4_MHZ = 2 # High Speed mode - 3.4 MHz
    SPEED_1_7_MHZ = 3 # High Speed mode 2 - 1.7 MHz
```

## SPISpeed
Definition of the speed of SPI bus.
```python
class SPISpeed:
    SPI_10_MHZ = 6
    SPI_7_5_MHZ = 8
    SPI_6_MHZ = 10
    SPI_5_MHZ = 12
    SPI_3_75_MHZ = 16
    SPI_3_MHZ = 20
    SPI_2_5_MHZ = 24
    SPI_2_MHZ = 30
    SPI_1_5_MHZ = 40
    SPI_1_25_MHZ = 48
    SPI_1_2_MHZ = 50
    SPI_1_MHZ = 60
    SPI_750_KHZ = 80
    SPI_600_KHZ = 100
    SPI_500_KHZ = 120
    SPI_400_KHZ = 150
    SPI_300_KHZ = 200
    SPI_250_KHZ = 240
```

## SPITransferBits
Definition of the SPI bits.
```python
class SPITransferBits:
    SPI8BIT = 8 # 8 bit register read/write
    SPI16BIT = 16 # 16 bit register read/write
```

## SPIMode
Definition of the SPI mode.
```python
class SPIMode:
    MODE0 = 0x00 # SPI Mode 0: CPOL=0; CPHA=0
    MODE1 = 0x01 # SPI Mode 1: CPOL=0; CPHA=1
    MODE2 = 0x02 # SPI Mode 2: CPOL=1; CPHA=0
    MODE3 = 0x03 # SPI Mode 3: CPOL=1; CPHA=1
```

## MultiIOPin
Definition of the shuttle board pin(s)
```python
class MultiIOPin(Enum):
    SHUTTLE_PIN_7 = 0x09 # CS pin
    SHUTTLE_PIN_8 = 0x05 # Multi-IO 5
    SHUTTLE_PIN_9 = 0x00 # Multi-IO 0
    SHUTTLE_PIN_14 = 0x01 # Multi-IO 1
    SHUTTLE_PIN_15 = 0x02 # Multi-IO 2
    SHUTTLE_PIN_16 = 0x03 # Multi-IO 3
    SHUTTLE_PIN_19 = 0x08 # Multi-IO 8
    SHUTTLE_PIN_20 = 0x06 # Multi-IO 6
    SHUTTLE_PIN_21 = 0x07 # Multi-IO 7
    SHUTTLE_PIN_22 = 0x04 # Multi-IO 4
    SHUTTLE_PIN_SDO = 0x1F
    # APP3.0 pins
    MINI_SHUTTLE_PIN_1_4 = 0x10 # GPIO0
    MINI_SHUTTLE_PIN_1_5 = 0x11 # GPIO1
    MINI_SHUTTLE_PIN_1_6 = 0x12 # GPIO2/INT1
    MINI_SHUTTLE_PIN_1_7 = 0x13 # GPIO3/INT2
    MINI_SHUTTLE_PIN_2_5 = 0x14 # GPIO4
    MINI_SHUTTLE_PIN_2_6 = 0x15 # GPIO5
    MINI_SHUTTLE_PIN_2_1 = 0x16 # CS
    MINI_SHUTTLE_PIN_2_3 = 0x17 # SDO
    MINI_SHUTTLE_PIN_2_7 = 0x1D # GPIO6
    MINI_SHUTTLE_PIN_2_8 = 0x1E # GPIO7
```

## SensorInterface
To define Sensor interface.
```python
class SensorInterface(Enum):
    SPI = 0
    I2C = 1
```

## I2CBus
Used to define the I2C type.
```python
class I2CBus(Enum):
    BUS_I2C_0 = 0
    BUS_I2C_1 = 1
    BUS_I2C_MAX = 2
```

## SPIBus
Used to define the SPI type.
```python
class SPIBus(Enum):
    BUS_SPI_0 = 0
    BUS_SPI_1 = 1
    BUS_SPI_MAX = 2
```

## PinInterruptMode
Defines Pin interrupt modes.
```python
class PinInterruptMode(Enum):
    # Trigger interrupt on pin state change
    PIN_INTERRUPT_CHANGE = 0
    # Trigger interrupt when pin changes from low to high
    PIN_INTERRUPT_RISING_EDGE = 1
    # Trigger interrupt when pin changes from high to low
    PIN_INTERRUPT_FALLING_EDGE = 2
    PIN_INTERRUPT_MODE_MAXIMUM = 4
```

## StreamingMode
Streaming mode definitions.
```python
class StreamingMode:
    STREAMING_MODE_POLLING = 0 # Polling mode streaming
    STREAMING_MODE_INTERRUPT = 1 # Interrupt mode streaming
```

## StreamingState
Streaming state definitions.
```python
class StreamingState:
    STREAMING_START = 1
    STREAMING_STOP = 0
```

## SamplingUnits
Sampling Unit definitions.
```python
class SamplingUnits:
    SAMPLING_TIME_IN_MICRO_SEC = 0x01 # sampling unit in micro second
    SAMPLING_TIME_IN_MILLI_SEC = 0x02 # sampling unit in milli second
```
