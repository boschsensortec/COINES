# coines_shuttle_eeprom_write
This API is used to write the content into shuttle eeprom.

```C
int16_t coines_shuttle_eeprom_write(uint16_t start_addr, uint8_t *buffer, uint16_t length);
```

Arguments:

- `start_addr` : EEPROM write address.
  
- `buffer` : Pointer to the buffer.
  
- `length` : Length of the buffer.

