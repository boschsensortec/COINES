# coines_config_i2s_bus
This API is used to configure the I2S bus to match the TDM configuration

```C
int16_t coines_config_i2s_bus(uint16_t data_words, coines_tdm_callback callback);
```

Arguments:

- `data_words`: number of words to use in the buffer. Max is set at `COINES_TDM_BUFFER_SIZE_WORDS`.
- `callback`: register a callback to be called to process and copy the data.