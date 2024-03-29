/**
 * Copyright (C) 2023 Bosch Sensortec GmbH
 *
 * SPDX-License-Identifier: BSD-3-Clause
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "coines.h"

/*! Macros to hold the BLE peripheral name and address to be connected */
/*! Please change the name and address with BLE name of the App board under test */
#define BLE_NAME  "APP Board 3.0(B6-E5)"
#define BLE_ADDR  "dd:fc:ab:af:b6:e5"

/*! Variable to hold the communication interface type */
const enum coines_comm_intf comm_intf = COINES_COMM_INTF_BLE;

/*!
 * @brief Exits by printing the error code
 * @param func_name
 * @param err_code
 */
void check_com_result(char *func_name, int16_t err_code)
{
    if (err_code != COINES_SUCCESS)
    {
        printf("\n%s exiting with Error_code: %d", func_name, err_code);
        exit(1);
    }
}

/*!
 * @brief API to initialize App board by establishing BLE connection
 * @param ble_name BLE peripheral name
 * @return Error code
 */
int16_t coines_board_init()
{
    struct coines_board_info board_info;
    struct ble_peripheral_info ble_config = {BLE_ADDR, ""};


    int16_t result = coines_open_comm_intf(comm_intf, &ble_config);

    check_com_result("Coines open", result);

    result = coines_get_board_info(&board_info);
    if (result == COINES_SUCCESS)
    {
        printf("\nBoard Info:");
        printf("\n\tboard_info.board:0x%02X", board_info.board);
        printf("\n\tboard_info.hardware_id:0x%02X", board_info.hardware_id);
        printf("\n\tboard_info.shuttle_id:0x%02X", board_info.shuttle_id);
        printf("\n\tboard_info.software_id:0x%02X", board_info.software_id);
    }

    coines_delay_msec(100);

    /* Power up the board */
    coines_set_shuttleboard_vdd_vddio_config(3300, 3300);

    coines_delay_msec(200);

    return result;
}

/*!
 * @brief API to deinitialize App board by closing BLE connection
 */
void coines_board_deinit(void)
{
    coines_set_shuttleboard_vdd_vddio_config(0, 0);
    coines_delay_msec(100);

    /* Coines interface reset */
    coines_soft_reset();
    coines_delay_msec(100);

    coines_close_comm_intf(comm_intf, NULL);
}

int main(void)
{
    uint8_t buffer_out[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int8_t result;

    struct ble_peripheral_info ble_info[40];
    uint8_t peripheral_count, i;

    /* Get the BLE peripheral list */
    int8_t scan_result = coines_scan_ble_devices(ble_info, &peripheral_count, 7000);

    check_com_result("Coines BLE scan", scan_result);

    /* Print the BLE peripheral list */
    printf("\nBLE devices found:");
    for (i = 0; i < peripheral_count; i++)
    {
        printf("\n[%d] %s [%s]", i, ble_info[i].ble_identifier, ble_info[i].ble_address);
    }

    /* Open BLE connection */
    coines_board_init();

    /* Test an echo command */
    result = coines_echo_test(buffer_out, sizeof(buffer_out));
    check_com_result("Coines echo", result);
    if (result == COINES_SUCCESS)
    {
        printf("\nEcho test: Success\n");
    }

    /* Close BLE connection */
    coines_board_deinit();

    return 0;
}
