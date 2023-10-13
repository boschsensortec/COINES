# coines_shuttle_eeprom_read
This API is used to read the content from shuttle eeprom.

```C
int16_t coines_shuttle_eeprom_read(uint16_t start_addr, uint8_t *buffer, 
    uint16_t length);
```

Arguments:

- `start_addr` : EEPROM read address.
 
- `buffer` : Pointer to the buffer.

- `length` : Length of the buffer.

