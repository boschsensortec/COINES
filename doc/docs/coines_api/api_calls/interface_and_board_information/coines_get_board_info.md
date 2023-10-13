# coines_get_board_info
Gets the board information.

```C
int16_t coines_get_board_info(struct coines_board_info *data);
```

The data structure contains the following items:

```C
struct coines_board_info {
	/*!Board hardware ID */
	uint16_t hardware_id;
	/*!Board software ID */
	uint16_t software_id;
	/*!Type of the board like APP2.0, Arduino Due*/
	uint8_t board;
	/*!Shuttle ID of the sensor connected*/
	uint16_t shuttle_id;
};
```