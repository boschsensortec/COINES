# coinespy API calls: GPIO oriented calls
      
## set_pin_config
Configures the state, level and direction of a GPIO pin

```python
coinesboard.set_pin_config(pin_number: MultiIOPin,direction: PinDirection,output_state: PinValue) -> ErrorCodes
```

For the definition of MultiIOPin, refer to [11.3.6.8](../definition_of_constants.md/#multiiopin). For the definition of PinDirection, refer to
[11.3.6.1](../definition_of_constants.md/#pindirection). For PinValue, refer to [11.3.6.2](../definition_of_constants.md/#pinvalue).

## get_pin_config
Obtains information regarding the Pin’s state, level and direction.

```python
PinConfigInfo = coinesboard.get_pin_config(pin_number: MultiIOPin)
# Return:
PinConfigInfo.direction # 0: INPUT, 1: OUTPUT
PinConfigInfo.switch_state # 0: OFF, 1: ON
PinConfigInfo.level # 1: HIGH, 0: LOW
```

## set_shuttleboard_vdd_vddio_config
Set the VDD and VDDIO voltage level.
                
```python
coinesboard.set_shuttleboard_vdd_vddio_config(vdd_val: float = None, vddio_val: float =
None) -> ErrorCodes
# Example: coinesboard.set_shuttleboard_vdd_vddio_config(3.3, 3.3)
```

## set_vdd
Set the VDD voltage level.

```python
coinesboard.set_vdd(vdd_val: float = None) -> ErrorCodes
# Example: coinesboard.set_vdd(3.3)
```

## set_vddio
Set the VDDIO voltage level.

```python
coinesboard.set_vddio(vdd_val: float = None) -> ErrorCodes
# Example: coinesboard.set_vddio(3.3)
```