# Cross compiling and downloading example to Nicla Sense ME's microcontroller

1. Make sure that [GNU Embedded Toolchain for ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) is installed on your PC and added to environmental variable `PATH`.
2. Connect the Nicla Sense ME board via USB.
3. Open the command prompt or the terminal.
4. Use the command cd to go to the directory where the example that is to be built is located.
5. Type mingw32-make TARGET=MCU_NICLA download . Other available options are:

    |Download example to NICLA MCU FLASH*| `mingw32-make LOCATION=FLASH TARGET=MCU_NICLA download`|
    |--------|--------|
    |**Compile for PC (Default)**| **`mingw32-make TARGET=PC`**|

    **NOTE**: Only Coines Bridge example supported in v2.8.8.