:: This script updates APP3.0 board with COINES Bridge firmware
:: Switching to bootloader mode is automatic !

@echo off
..\..\..\tools\app_switch\app_switch usb_dfu_bl
..\..\..\tools\usb-dfu\dfu-util --device -,108c:ab39 -a FLASH -D coines_bridge_flash_firmware.bin -R
pause