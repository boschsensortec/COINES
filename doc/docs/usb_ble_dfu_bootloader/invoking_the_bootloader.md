# Invoking the Bootloader

APP3.0 Board
- Hardware
	1. Turn OFF and ON the board with T2 pressed, blue LED glows indicating that the board switched to bootloader mode.
- Software
	1. Write 0x4E494F43 ('N','I','O','C') to MAGIC\_LOCATION (0x2003FFF4)
	2. Write 0x0 or 0xF0000 to APP\_START\_ADDR (0x2003FFF8)
	3. Call NVIC\_SystemReset()
	4. Invoke Bootloader from Software

	```C
	#define  MAGIC_LOCATION (0x2003FFF4)
	#define  APP_START_ADDR (*(uint32_t *)(MAGIC_LOCATION+4)
 
	*((uint32_t *)MAGIC_LOCATION) == 0x4E494F43;
	APP_START_ADDR = 0xF0000;
	//APP_START_ADDR = 0x0;
	NVIC_SystemReset();	
	```
	5. The same feature can also be used to perform application switch ( 2 or more applications can reside in the same flash memory at different address locations ).
	Just write the application start address to APP\_START\_ADDR instead of bootloader address


Nicla Sense ME Board
- Hardware
	1. Press three times reset button, blue LED glows indicating that the board switched to
	bootloader mode.

- Software
	1. Write 0x4E494F43 (’N’,’I’,’O’,’C’) to MAGIC_LOCATION (0x2000F804)
	2. Call NVIC_SystemReset()
	3. Invoke Bootloader from Software

	```C
	#define MAGIC_LOCATION (0x2000F804)
	#define APP_START_ADDR (*(uint32_t *)(MAGIC_LOCATION+4)
	*((uint32_t *)MAGIC_LOCATION) == 0x544F4F42;
	NVIC_SystemReset();
	```	

	4. The same feature can also be used to perform application switch ( 2 or more applications can reside in the same flash memory at different address locations ).Just write the application start address to APP_START_ADDR instead of bootloader address


