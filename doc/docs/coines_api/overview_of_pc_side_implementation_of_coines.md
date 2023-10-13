# Overview of PC side implementation of COINES

Bosch Sensortec recommends using the SensorAPI in order to communicate with the sensors.
The SensorAPI , an abstraction layer written in C makes it much more convenient for the user to access the register map of the sensor in order to configure certain functionality and obtain certain information from it.

For making use of the SensorAPI, three function pointers must be set to the appropriate read/write functions of the selected bus on the system (either I~2~C or SPI), as well as one function pointer to a system's function causing delays in milliseconds.

In order to execute C code using SensorAPI on a PC, the coinesAPI provides the mentioned read,write,delay functions. These functions are wrapper functions, embedding the actual SensorAPI payloads into a transport package, sending this via USB to the APP2.0, where the payload is translated into corresponding SPI or I~2~C messages and sent to the sensor on the shuttle board.
The mapping would look similar to the one below.

```C
#include "bst_sensor.h"

struct bst_sensor_dev sensordev;
....
....
sensordev.dev_id = I2C_ADDR;        // SPI - CS PIN
sensordev.read = coines_read_i2c;   // coines_read_spi
sensordev.write = coines_write_i2c; // coines_write_spi
sensordev.delay_ms = coines_delay_msec;
```

Using this method, the full functionality of the SensorAPI can be used on PC side, sample code can be modified and tested, and data can be logged in a convenient way.

This setup has the challenge of lacking the real-time capabilities known from a pure microcontroller environment.
To overcome this, the coinesAPI offers streaming functions, which allow the user to schedule data readout directly on the microcontroller, either based on a data interrupt coming from the sensors or based on the timer of the microcontroller.
The scheduler waits for the configured interrupt (sensor interrupt or timer interrupt) and reads out areas of the register map, which can be configured by the user.

As an example, the user could choose to read out the 6 bytes from the register map of a certain inertial sensor, containing the sensor data of three axis (2 bytes per axis).
If the user would configure for example a readout once per milliseconds, the result would be a data stream of three-axis sensor data at a rate of 1 kHz.