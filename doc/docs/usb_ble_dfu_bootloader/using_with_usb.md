# Using the Bootloader via USB

Write firmware to Flash memory using following command

- dfu-util -a FLASH -D fw.bin -R

Write firmware to RAM memory using following command

- dfu-util -a RAM -D fw.bin -R

Read firmware from Flash memory using following command

- dfu-util -a FLASH -U fw\_bkup.bin

Read firmware from RAM memory using following command

- dfu-util -a RAM -U fw\_bkup.bin

Read device serial number/ BLE MAC address

- dfu-util -l

**Note** : Not applicable for Nicla Sense ME board
