# coines_attach_timed_interrupt
Attaches a timed interrupt to a Multi-IO pin.

```C
int16_t coines_attach_timed_interrupt(enum coines_multi_io_pin pin_number, 
    void (*timed_interrupt_cb)(uint64_t,uint32_t,uint32_t), enum coines_pin_interrupt_mode
    int_mode);
```

Arguments:

- `pin_number`: Multi-IO pin.
- `timed_interrupt_cb`:  Name of the function to be called on detection of interrupt.
- `int_mode`: Trigger modes - change, rising edge,  falling edge.

