# Running examples on PC side

When compiling the examples for PC side, the COINES layer provides an abstraction of the embedded environment on the host side.
COINES library provides read and write functions for I~2~C and SPI on PC side.
These functions receive the arguments of the user input (i.e. what register address to read from) and tunnel them through the USB connection to the Application Board, where they are fed into the embedded I~2~C and SPI functions and are executed to access the sensor
Any result or response from those functions is tunneled back to the PC side and provided to the example application.

This approach allows easy and flexible programming and offers the possibility to integrate the example code into other applications or add advanced logging options.
The drawback is that in this mode the code is not executed in real time, as it runs on a multi-tasking operating system
To overcome this drawback, the examples can also be run on the MCU side (see next section).

<figure markdown>

  ![Image: running example on PC side](working_princpile_run_on_pc.drawio)
  <figcaption>Fig. 4: Working principle: running example on PC side</figcaption>
</figure>