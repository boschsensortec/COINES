# Using the Bootloader via BLE

- PC (Windows/Linux and macOS)  
Python script present in following path `COINES\v2.6.0\tools\app30-ble-dfu` can use the binary file directly.
	1. Scan for devices to find BLE MAC address using below command.
   
		- python app30-ble-dfu.py -l
  
	2. Update firmware by using MAC address obtained in the previous step and firmware BIN file.
   
		- python app30-ble-dfu.py -d D7:A3:CE:8E:36:14 -f firmware.bin
  
- Android devices
  
	1. Generate ZIP package using [https://pypi.org/project/adafruit-nrfutil/](https://pypi.org/project/adafruit-nrfutil/) before using nRF ToolBox for BLE or nRF connect for mobile.
   
		- adafruit-nrfutil dfu genpkg --dev-type 0x0052 --application firmware.bin dfu-package.zip

	**Note** : Not applicable for Nicla Sense ME board