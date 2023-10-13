# coines_attach_interrupt
Attaches an interrupt to a Multi-IO pin. Works only on MCU.

```C
void coines_attach_interrupt(enum coines_multi_io_pin pin_number,void (*callback)(uint32_t, uint32_t),enum coines_pin_interrupt_mode int_mode);
```

Arguments:

- `pin_number`:  Multi-IO pin
- `callback`: Name of the function to be called on detection of interrupt
- `int_mode`: Trigger modes - change (`COINES_PIN_INTERRUPT_CHANGE`),  
rising edge (`COINES_PIN_INTERRUPT_RISING_EDGE`),  
falling edge (`COINES_PIN_INTERRUPT_FALLING_EDGE`)