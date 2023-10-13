# FAQ

## 1. I want to upgrade APP2.0/APP3.0 firmware.

- Use `app20-flash` tool (or) Development Desktop to upgrade APP2.0 firmware.
- Use `dfu-util` tool to upgrade APP3.0 firmware.

## 2. Why GCC is chosen as the compiler?
GCC is widely used and available in both Linux and Windows environments.
However, if the user uses a different compiler, it should be easy to migrate the code, since no compiler-specific tweaks are needed.

## 3. Why do you use TDM-GCC in Windows?
It is a complete toolchain in a single installer, but does not come with too much overhead the COINES user most likely does not need.
The installation procedures for other toolchains are more complicated and especially for in-experienced users difficult to handle.

## 4. Why do you use mingw32-make in Windows?
It comes as a part of TDM-GCC package and can handle Windows path names better compared e.g. with MSYS make.
The usage of spaces in path names can be overcome using 8.3 naming format.

## 5. What to do in case of any communication or initialization failure while running examples?
Resetting or rebooting the board will help solving this.	

## 6. What does 'app_switch' tool do?
'app_switch' tool can command the Application Board to jump to a specified address on RAM or FLASH.
It works only with APP2.0 firmware v3.1 or later.
COINES uses this feature to jump to USB DFU Bootloader or example application.

## 7. Are libraries provided by microcontroller vendor used for COINES on MCU implementation ?
Yes ! ASF v3.42 (Advanced Software Framework) and nRF5 SDK v15.2 is being used for APP2.0 and APP3.0.
One can download the latest version of libraries from the below links

- [https://www.microchip.com/mplab/avr-support/advanced-software-framework](https://www.microchip.com/mplab/avr-support/advanced-software-framework)
- [https://developer.nordicsemi.com/nRF5_SDK/](https://developer.nordicsemi.com/nRF5_SDK/)

## 8. How is the binary file from PC downloaded to RAM or Flash memory of MCU?
USB DFU protocol and open-source 'dfu-util' is used.

- USB DFU Specification - [https://www.usb.org/sites/default/files/DFU_1.1.pdf](https://www.usb.org/sites/default/files/DFU_1.1.pdf)
- dfu-util Homepage - [http://dfu-util.sourceforge.net/](http://dfu-util.sourceforge.net/)

## 9. Why is there no output in my terminal application not stream data after cross-compiling and downloading an example on the MCU?
The code example on the MCU waits until the serial port of the board is opened.
However, opening the port is not enough, the user has to ensure that also the DTR signal is set (this is required due to have higher compatibiliy among different terminal applications).

## 10. Why can some examples only be compiled for either PC or MCU target?

- Examples which make use of APIs like `coines_config_streaming`, `coines_read_stream_sensor_data` etc., are meant to work only on PC.
- Use of APIs like `coines_attach_interrupt` in example will make it only compatible with MCU.  
- Constraints can also be introduced by the use of POSIX C library. Eg:Functions from `time.h`, `pthread.h`, etc.
