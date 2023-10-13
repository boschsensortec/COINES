# GPIO mapping of APP2.0 shuttle board pins


The APP2.0 shuttle board has total 28 pins, of which some have a predefined functionality and some can be used as GPIO by the user.

The shuttle board connector details are given in the table below:


| Pin number on shuttle board | Name / function | Pin number on shuttle board | Name/function |
|:---:|----------------------|:----:|---|
| 1   | VDD (3.3V)           | 28   | SHTLE_COD #4 | 
| 2   | VDDIO (3.3V)         | 27   | SHTLE_COD #3 | 
| 3   | GND                  | 26   | SHTLE_COD #2 | 
| 4   | SPI MISO             | 25   | SHTLE_COD #1 | 
| 5   | SPI: MOSI / I~2~C: SDA | 24   | SHTLE_COD #0 | 
| 6   | SPI: SCK / I~2~C: SCL  | 23   | SHTLE_COD_GND | 
| 7   | SPI: CS              | 22   | IO_4 ( GPIO #4 ) | 
| 8   | IO_5 ( GPIO #5 )     | 21   | IO_7 ( GPIO #7 ) | 
| 9   | IO_0 ( GPIO #0 )     | 20   | IO_6 ( GPIO #6 ) |  
| 10  | SHTLE_COD #5         | 19   | IO_8 ( GPIO #8 ) |  
| 11  | SHTLE_COD #6         | 18   | SCL (see note) |  
| 12  | SHTLE_COD #7         | 17   | SDA (see note)|  
| 13  | SHTLE_COD #8         | 16   | IO_3 ( GPIO #3 ) | 
| 14  | IO_1 ( GPIO #1 )     | 15   | IO_2 ( GPIO #2 ) |



Table 1: Overview of shuttle board pins and their functions

**Note**:

- In coinesAPI the pins are addressed using the same numbers as on the shuttle board.
For example, the GPIO #5 has the pin number 8.
- In some cases (depending on the sensor), the I~2~C lines are shuttle board pin 6 for the clock signal SCL and shuttle board pin 5 for the data line SDA.
In such cases pins 17 and 18 may not be connected.
Please carefully read the shuttle board documentation.