import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_updowncounter(dut):

    # Start clock
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())

    # Initial values
    dut.ena.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Hold reset
    for _ in range(5):
        await RisingEdge(dut.clk)

    # Release reset
    dut.rst_n.value = 1

    # Keep disabled after reset
    await RisingEdge(dut.clk)

    # Check reset value
    assert int(dut.uo_out.value) == 0, "Reset failed"

    # Enable counter
    dut.ena.value = 1

    # -------------------------
    # UP COUNT
    # -------------------------
    dut.ui_in.value = 1

    for i in range(1, 6):
        await RisingEdge(dut.clk)
        assert int(dut.uo_out.value) == i, f"UP count failed at {i}"

    # -------------------------
    # DOWN COUNT
    # -------------------------
    dut.ui_in.value = 0

    expected = 4

    for _ in range(5):
        await RisingEdge(dut.clk)
        assert int(dut.uo_out.value) == expected, \
            f"DOWN count failed at {expected}"
        expected -= 1
