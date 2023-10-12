# Installation of compiler environment

On a Debian or Redhat based Linux distro, the installer prompts for installation of missing dependencies, `gcc`, `make` and `libusb-dev` packages.
If due to some reason installation fails,the user can manually install the dependencies.

- Debian based distros - `gcc`, `make`, `libusb-1.0-0-dev`, `dfu-util` 
- Redhat based distros - `gcc`, `make`, `libusbx-devel`, `dfu-util`
- MacOS - `libusb`, `dfu-util`

If you intend to run the COINES example on Application Board's microcontroller, download the latest version of [GNU Embedded Toolchain for ARM](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads) for Linux and extract the package.
Add the compiler to PATH variable by editing `$HOME/.bashrc` or similar file like `/etc/profile` or `/etc/environment`.