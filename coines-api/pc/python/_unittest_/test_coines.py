#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=missing-function-docstring, protected-access, unused-argument
"""
This is a simple example of coinespy to verify the basic details
The test to be performed with app3.0/app2.0 board plugged-in
"""
import platform
from unittest import mock
import os
import ctypes as ct
import pytest
import coinespy as cpy
from coinespy import ErrorCodes

BOARD = cpy.CoinesBoard()
INTERFACE = cpy.CommInterface.USB


def test_open_comm_interface():
    BOARD._lib.coines_open_comm_intf = mock.Mock(return_value=0)
    ret = BOARD.open_comm_interface(INTERFACE)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_open_comm_interface_with_args():
    BOARD._lib.coines_open_comm_intf = mock.Mock(return_value=0)
    serial_com_config = cpy.SerialComConfig(
        com_port_name="COM1",
        baud_rate=115200,
        vendor_id=1234,
        product_id=5678,
        rx_buffer_size=256
    )
    ret = BOARD.open_comm_interface(INTERFACE, serial_com_config=serial_com_config)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_get_board_info_app30():
    BOARD._lib.coines_get_board_info = mock.Mock(return_value=0)
    BOARD.get_board_info()
    assert BOARD.error_code == ErrorCodes.COINES_SUCCESS


def test_set_pin_config():
    mock_func = mock.Mock(return_value=0)
    BOARD.wrap_function = mock.Mock(return_value=mock_func)
    BOARD._lib.coines_set_pin_config = mock.Mock(return_value=0)
    ret = BOARD.set_pin_config(cpy.MultiIOPin.SHUTTLE_PIN_7, cpy.PinDirection.OUTPUT, cpy.PinValue.HIGH)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_get_pin_config():
    mock_func = mock.Mock(return_value=0)
    BOARD.wrap_function = mock.Mock(return_value=mock_func)
    BOARD._lib.coines_get_pin_config = mock.Mock(return_value=0)
    BOARD.get_pin_config(cpy.MultiIOPin.SHUTTLE_PIN_7)
    assert BOARD.error_code == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("vdd,vddio,exp_vdd,exp_vddio",
                         [(3.3, 3.3, ct.c_ushort(3300), 3300), (0, 0, 0, 0), (3.3, 0, 3300, 0), (0, 3.3, 0, 3300)])
def test_set_shuttleboard_vdd_vddio_config(vdd, vddio, exp_vdd, exp_vddio):
    BOARD._lib.coines_set_shuttleboard_vdd_vddio_config = mock.Mock(return_value=0)
    ret = BOARD.set_shuttleboard_vdd_vddio_config(vdd_val=vdd, vddio_val=vddio)
    # assert BOARD.current_vdd == exp_vdd
    # assert BOARD.current_vddio == exp_vddio
    assert ret == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("vdd", [0, 3.3])
def test_set_vdd(vdd):
    BOARD._lib.coines_set_shuttleboard_vdd_vddio_config = mock.Mock(return_value=0)
    ret = BOARD.set_vdd(vdd_val=vdd)
    # assert BOARD.current_vdd == vdd
    assert ret == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("vddio", [0, 3.3])
def test_set_vddio(vddio):
    BOARD._lib.coines_set_shuttleboard_vdd_vddio_config = mock.Mock(return_value=0)
    ret = BOARD.set_vddio(vddio_val=vddio)
    # assert BOARD.current_vddio == vddio
    assert ret == ErrorCodes.COINES_SUCCESS


# ########################## I2C ##########################
def test_config_i2c_bus():
    BOARD._lib.coines_config_i2c_bus = mock.Mock(return_value=0)
    ret = BOARD.config_i2c_bus(cpy.I2CBus.BUS_I2C_0, 0x18, cpy.I2CMode.STANDARD_MODE)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_write_i2c():
    BOARD._lib.coines_write_i2c = mock.Mock(return_value=0)
    ret = BOARD.write_i2c(cpy.I2CBus.BUS_I2C_0, 0x7C, 0, 0x18)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_read_i2c():
    BOARD._lib.coines_read_i2c = mock.Mock(return_value=0)
    ret = BOARD.read_i2c(cpy.I2CBus.BUS_I2C_0, 0x12 & 0x7F)
    # reg_data = BOARD.read_i2c(BUS, 0x12 & 0x7F)
    # assert reg_data == [0]
    assert ret in ([0], 0)


def test_deconfig_i2c_bus():
    BOARD._lib.coines_deconfig_i2c_bus = mock.Mock(return_value=0)
    ret = BOARD.deconfig_i2c_bus(cpy.I2CBus.BUS_I2C_0)
    assert ret == ErrorCodes.COINES_SUCCESS


# ########################## SPI ##########################
def test_config_spi_bus():
    BOARD._lib.coines_config_spi_bus = mock.Mock(return_value=0)
    ret = BOARD.config_spi_bus(cpy.SPIBus.BUS_SPI_0, cpy.MultiIOPin.SHUTTLE_PIN_7,
                               cpy.SPISpeed.SPI_1_MHZ, cpy.SPIMode.MODE0)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_write_spi():
    BOARD._lib.coines_write_spi = mock.Mock(return_value=0)
    ret = BOARD.write_spi(cpy.SPIBus.BUS_SPI_0, 0x19, 0x02, 9)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_read_spi():
    BOARD._lib.coines_read_spi = mock.Mock(return_value=0)
    ret = BOARD.read_spi(cpy.SPIBus.BUS_SPI_0, 0X00)
    assert ret in ([0], 0)


def test_custom_spi_config():
    BOARD._lib.coines_config_spi_bus = mock.Mock(return_value=0)
    ret = BOARD.custom_spi_config(cpy.SPIBus.BUS_SPI_0, cpy.MultiIOPin.SHUTTLE_PIN_7,
                                  cpy.SPISpeed.SPI_1_MHZ, cpy.SPIMode.MODE0)
    assert ret == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("spi_bits", [cpy.SPITransferBits.SPI16BIT, cpy.SPITransferBits.SPI8BIT])
def test_config_word_spi_bus(spi_bits):
    BOARD._lib.coines_config_word_spi_bus = mock.Mock(return_value=0)
    ret = BOARD.config_word_spi_bus(cpy.SPIBus.BUS_SPI_0, cpy.MultiIOPin.SHUTTLE_PIN_7,
                                    cpy.SPISpeed.SPI_1_MHZ, cpy.SPIMode.MODE0, spi_bits)
    assert ret == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("sensor_interface", [cpy.SensorInterface.I2C.value, cpy.SensorInterface.SPI.value])
def test_read_16bit_spi(sensor_interface):
    BOARD._lib.coines_read_16bit_spi = mock.Mock(return_value=0)
    BOARD._sensor_interface = sensor_interface
    if BOARD._sensor_interface == cpy.SensorInterface.SPI.value:
        BOARD.read_16bit_spi(cpy.SPIBus.BUS_SPI_0, 0X00)
        assert BOARD.error_code == ErrorCodes.COINES_SUCCESS
    else:
        with pytest.raises(RuntimeError, match='No bus configured'):
            BOARD.read_16bit_spi(cpy.SPIBus.BUS_SPI_0, 0X00)


def test_write_16bit_spi():
    BOARD._lib.coines_write_16bit_spi = mock.Mock(return_value=0)
    ret = BOARD.write_16bit_spi(cpy.SPIBus.BUS_SPI_0, 0x00, [0x10])
    assert ret == ErrorCodes.COINES_SUCCESS


def test_deconfig_spi_bus():
    BOARD._lib.coines_deconfig_spi_bus = mock.Mock(return_value=0)
    ret = BOARD.deconfig_spi_bus(cpy.SPIBus.BUS_SPI_0)
    assert ret == ErrorCodes.COINES_SUCCESS


# ########################## Other Functions ##########################
def test_passing_dll():
    libs = {
        "Windows": {"32bit": "libcoines_32.dll", "64bit": "libcoines_64.dll"},
        "Linux": {"32bit": "libcoines_32.so", "64bit": "libcoines_64.so"},
        "Mac": {"32bit": "libcoines_32.dylib", "64bit": "libcoines.dylib"}
    }
    _platform = platform.system()
    _platform = "Mac" if _platform not in ("Windows", "Linux") else _platform
    arch = platform.architecture()[0]
    board = cpy.CoinesBoard(path_to_coines_lib=f"coinespy/{libs[_platform][arch]}")
    assert os.path.split(board._lib._name)[-1] == libs[_platform][arch]


def test_none_dll():
    with pytest.raises(SystemExit, match="-1"):
        cpy.CoinesBoard(r"coinespy/libcoines_6.dll")


@pytest.mark.skipif(platform.architecture()[0] == "32bit" or platform.system() != 'Windows',
                    reason="Not applicable for 32bit architecture")
def test_wrap_function():
    board = cpy.CoinesBoard(r"coinespy/libcoines_64.dll")
    ret = board.wrap_function('coines_set_pin_config', ct.c_uint8, [ct.c_uint8, ct.c_uint8, ct.c_uint8])
    assert ret.restype == ct.c_ubyte


def test_close_comm_interface():
    BOARD._lib.coines_close_comm_intf = mock.Mock(return_value=0)
    ret = BOARD.close_comm_interface()
    assert ret == ErrorCodes.COINES_SUCCESS


def test_soft_reset():
    BOARD._lib.coines_soft_reset = mock.Mock(return_value=0)
    BOARD.soft_reset()
    BOARD._lib.coines_soft_reset.assert_called_once()


def test_delay_milli_sec():
    BOARD._lib.coines_delay_msec = mock.Mock(return_value=0)
    BOARD.delay_milli_sec(1000)
    BOARD._lib.coines_delay_msec.assert_called_once()


def test_delay_micro_sec():
    BOARD._lib.coines_delay_usec = mock.Mock(return_value=0)
    BOARD.delay_micro_sec(1000)
    BOARD._lib.coines_delay_usec.assert_called_once()


def test_flush_interface():
    BOARD._lib.coines_flush_intf = mock.Mock(return_value=0)
    BOARD.flush_interface()
    BOARD._lib.coines_flush_intf.assert_called_once()


def test_config_streaming():
    BOARD._lib.coines_config_streaming = mock.Mock(return_value=0)
    ret = BOARD.config_streaming(0, cpy.StreamingConfig(), cpy.StreamingBlocks())
    assert ret == ErrorCodes.COINES_SUCCESS


def test_start_stop_streaming():
    BOARD._lib.coines_start_stop_streaming = mock.Mock(return_value=0)
    ret = BOARD.start_stop_streaming(0, 1)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_read_stream_sensor_data():
    BOARD._lib.coines_read_stream_sensor_data = mock.Mock(return_value=0)
    ret = BOARD.read_stream_sensor_data(0, 10)
    assert ret[0] == ErrorCodes.COINES_SUCCESS


def test_trigger_timer():
    BOARD._lib.coines_trigger_timer = mock.Mock(return_value=0)
    ret = BOARD.trigger_timer(0, 0)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_echo_test():
    BOARD._lib.coines_echo_test = mock.Mock(return_value=0)
    ret = BOARD.echo_test([])
    assert ret == ErrorCodes.COINES_SUCCESS


@pytest.mark.parametrize("code,err_statement", [(-1, ErrorCodes.COINES_E_FAILURE),
                                                (255, ErrorCodes.COINES_E_FAILURE),
                                                (0, ErrorCodes.COINES_SUCCESS),
                                                (257, ErrorCodes.COINES_E_UNDEFINED_CODE),
                                                (65531, ErrorCodes.COINES_E_DEVICE_NOT_FOUND)
                                                ])
def test_convert_to_signed_error_code(code, err_statement):
    ret = BOARD.convert_to_signed_error_code(code)
    assert ret == err_statement

# BLE com tests


INTERFACE = cpy.CommInterface.BLE


def test_open_ble_comm_interface_with_args():
    BOARD._lib.coines_open_comm_intf = mock.Mock(return_value=0)
    ble_com_config = cpy.BleComConfig()
    ret = BOARD.open_comm_interface(INTERFACE, ble_com_config=ble_com_config)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_open_ble_comm_interface():
    BOARD._lib.coines_open_comm_intf = mock.Mock(return_value=0)
    ret = BOARD.open_comm_interface(INTERFACE)
    assert ret == ErrorCodes.COINES_SUCCESS


def test_scan_ble_devices():
    BOARD._lib.coines_scan_ble_devices = mock.Mock(return_value=0)
    _, _ = BOARD.scan_ble_devices(0)
    assert BOARD.error_code == ErrorCodes.COINES_SUCCESS
