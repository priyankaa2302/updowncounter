import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ReadOnly


@cocotb.test()
async def test_updowncounter(dut):

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

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
    await ReadOnly()

    # Check reset value
    assert int(dut.uo_out.value) == 0

    # Enable counter
    dut.ena.value = 1

    # ---------------- COUNT UP ----------------
    dut.ui_in.value = 1

    for i in range(1, 6):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.uo_out.value) == i

    # ---------------- COUNT DOWN ----------------
    dut.ui_in.value = 0

    for i in range(4, -1, -1):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.uo_out.value) == i
