import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_updowncounter(dut):

    # Start clock
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.rst_n.value = 0
    dut.ena.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Hold reset
    for _ in range(5):
        await RisingEdge(dut.clk)

    # Release reset
    dut.rst_n.value = 1

    await RisingEdge(dut.clk)

    # Verify reset output
    assert int(dut.uo_out.value) == 0

    # Enable counter
    dut.ena.value = 1

    # --------------------
    # UP COUNT TEST
    # --------------------
    dut.ui_in.value = 1

    # wait one clock for update
    await RisingEdge(dut.clk)

    for i in range(1, 6):
        assert int(dut.uo_out.value) == i, \
            f"UP count failed at {i}"

        await RisingEdge(dut.clk)

    # --------------------
    # DOWN COUNT TEST
    # --------------------
    dut.ui_in.value = 0

    # wait one clock for update
    await RisingEdge(dut.clk)

    expected = 4

    while expected >= 0:

        assert int(dut.uo_out.value) == expected, \
            f"DOWN count failed at {expected}"

        expected -= 1

        await RisingEdge(dut.clk)

    dut._log.info("TEST PASSED")
