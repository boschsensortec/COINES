# Installation

The coinespy module can be installed using pip:

```bash
pip install coinespy
```

Linux users may have to use the below commands due to co-existence of Python 2.7 and Python 3.x

```bash
pip3 install coinespy
python3 -m pip install coinespy
```

The module can be found on [https://pypi.org/project/coinespy/](https://pypi.org/project/coinespy/) and also in the COINES installation folder, precisely in the subfolder `coines-api\pc\python`, in which a python wheel package is placed. 

It is highly recommended that the user is testing the following script (can be found as
`examples\python\coinespy_test.py` in the COINES installation) to check if the installation was
successful:

```python
import coinespy as cpy
from coinespy import ErrorCodes

COM_INTF = cpy.CommInterface.USB

if __name__ == "__main__":
    board = cpy.CoinesBoard()
    print(’coinespy version - %s’ % cpy.__version__)
    board.open_comm_interface(COM_INTF)
    if board.error_code != ErrorCodes.COINES_SUCCESS:
        print(f’Could not connect to board: {board.error_code}’)
    else:
        b_info = board.get_board_info()
        print(f"coines lib version: {board.lib_version}")
        print(f’BoardInfo: HW/SW ID: {hex(b_info.HardwareId)}/{hex(b_info.SoftwareId)}’)
        board.close_comm_interface()
```