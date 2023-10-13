# Invoking the Bootloader

## APP3.0 Board

- Hardware

	- Turn OFF and ON the board with T2 pressed, blue LED glows indicating that the board switched to bootloader mode.
   
- Software
  
	- Write 0x4E494F43 ('N','I','O','C') to MAGIC\_LOCATION (0x2003FFF4)
   
	- Write 0x0 or 0xF0000 to APP\_START\_ADDR (0x2003FFF8)
   
	- Call NVIC\_SystemReset()
   
	- Invoke Bootloader from Software

	```C
	#define  MAGIC_LOCATION (0x2003FFF4)
	#define  APP_START_ADDR (*(uint32_t *)(MAGIC_LOCATION+4)
 
	*((uint32_t *)MAGIC_LOCATION) == 0x4E494F43;
	APP_START_ADDR = 0xF0000;
	//APP_START_ADDR = 0x0;
	NVIC_SystemReset();	
	```

	- The same feature can also be used to perform application switch ( 2 or more applications can reside in the same flash memory at different address locations ).
	Just write the application start address to APP\_START\_ADDR instead of bootloader address.


## Nicla Sense ME Board

- Hardware
  
	- Press three times reset button, blue LED glows indicating that the board switched to
	bootloader mode.

- Software
  
	- Write 0x4E494F43 (’N’,’I’,’O’,’C’) to MAGIC_LOCATION (0x2000F804)
   
	- Call NVIC_SystemReset()
   
	- Invoke Bootloader from Software

	```C
	#define MAGIC_LOCATION (0x2000F804)
	#define APP_START_ADDR (*(uint32_t *)(MAGIC_LOCATION+4)
	*((uint32_t *)MAGIC_LOCATION) == 0x544F4F42;
	NVIC_SystemReset();
	```	

	- The same feature can also be used to perform application switch ( 2 or more applications can reside in the same flash memory at different address locations ).Just write the application start address to APP_START_ADDR instead of bootloader address.


