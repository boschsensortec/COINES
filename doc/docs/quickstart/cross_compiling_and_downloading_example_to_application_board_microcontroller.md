# Cross compiling and downloading example to Application Board's microcontroller

1. Make sure that [GNU Embedded Toolchain for ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) is installed on your PC and added to evironmental variable `PATH`.
2. Connect the Application board via USB, with the sensor shuttle board mounted.
3. Open the command prompt or the terminal.
4. Use the command `cd` to go to the directory where the example that is to be built is located. 
5. Type `mingw32-make TARGET=MCU_APP20 download`. Other available options are:

    |Cross-compile for APP2.0 board | `mingw32-make TARGET=MCU_APP20`|
    |--------|--------|
    |**Download example to APP2.0 MCU RAM**| **`mingw32-make LOCATION=RAM TARGET=MCU\_APP20 download`**|
    |**Download example to APP2.0 MCU FLASH**| **`mingw32-make LOCATION=FLASH TARGET=MCU\_APP20 download`**|
    |**Download example to APP3.0 MCU RAM**| **`mingw32-make LOCATION=RAM TARGET=MCU\_APP30 download`**|
    |**Download example to APP3.0 MCU FLASH***| **`mingw32-make LOCATION=FLASH TARGET=MCU\_APP30 download`**|
    |**Download example to APP3.0 MCU FLASH**| **`mingw32-make LOCATION=FLASH TARGET=MCU\_APP30 download`**|
    |**Compile for PC (Default)**| **`mingw32-make TARGET=PC`**|
    |**Run an example already residing in APP2.0 Flash memory**| **`mingw32-make run`**|
  
 
    Linux/MacOS/Cygwin/MSYS2 users can use `make`.

    **NOTE**: Downloading COINES example to APP3.0 Flash memory will overwrite default firmware.


6. Use a Serial Terminal application to view output.
	  - Windows - PuTTY, HTerm,etc.,
	  - Linux - `cat` command. Eg: `cat /dev/ttyACM0`
	  - macOS - `screen` command. Eg: `screen /dev/tty.usbmodem9F31`
7. For bluetooth, use [Serial Bluetooth terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal).

**Note**:

- Some examples may not compile for both PC and MCU target.
Please refer to the example documentation or simply the example name (e.g. examples that can only be compiled for the PC are named with a following '_pc').
- The binary on the MCU will be executed once the serial port is opened. The port must be opened including DTR signal set, otherwise the binary will not be executed. Some terminal programs such as HTerm allow explicit setting of the DTR signal.
- For printing over APP3.0 bluetooth interface, use `fprintf(bt_w,...)`.

