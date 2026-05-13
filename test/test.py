import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_updowncounter(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Initial values
    dut.rst_n.value = 0
    dut.ena.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    for _ in range(5):
        await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    await RisingEdge(dut.clk)

    assert int(dut.uo_out.value) == 0

    # Enable counter
    dut.ena.value = 1

    # -------------------
    # UP COUNT
    # -------------------
    dut.ui_in.value = 1

    for i in range(1, 6):
        await RisingEdge(dut.clk)
        assert int(dut.uo_out.value) == i, \
            f"UP count failed at {i}"

    # -------------------
    # DOWN COUNT
    # -------------------
    dut.ui_in.value = 0

    for i in range(4, -1, -1):
        await RisingEdge(dut.clk)
        assert int(dut.uo_out.value) == i, \
            f"DOWN count failed at {i}"

    dut._log.info("TEST PASSED")
