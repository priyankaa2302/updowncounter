# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_updowncounter(dut):
    dut._log.info("Start Up/Down Counter Test")

    # Clock: 10 us period (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # --------------------
    # RESET
    # --------------------
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, "Reset failed"

    # --------------------
    # UP COUNT TEST
    # ui_in[0] = 1 → count up
    # --------------------
    dut._log.info("Counting UP")
    dut.ui_in.value = 1

    for i in range(1, 6):
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == i, f"UP count failed at {i}"

    # --------------------
    # DOWN COUNT TEST
    # ui_in[0] = 0 → count down
    # --------------------
    dut._log.info("Counting DOWN")
    dut.ui_in.value = 0

    for i in range(5, 0, -1):
        await ClockCycles(dut.clk, 1)
        assert dut.uo_out.value == i - 1, f"DOWN count failed at {i}"

    dut._log.info("Test completed successfully")
