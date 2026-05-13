`timescale 1ns/1ps
`default_nettype none

module tb;

    reg clk;
    reg rst_n;
    reg ena;
    reg [7:0] ui_in;
    reg [7:0] uio_in;

    wire [7:0] uo_out;
    wire [7:0] uio_out;
    wire [7:0] uio_oe;

    tt_um_updowncounter dut (
        .ui_in(ui_in),
        .uo_out(uo_out),
        .uio_in(uio_in),
        .uio_out(uio_out),
        .uio_oe(uio_oe),
        .ena(ena),
        .clk(clk),
        .rst_n(rst_n)
    );

    initial begin
        $dumpfile("tb.vcd");
        $dumpvars(0, tb);
    end

    always #5 clk = ~clk;

    initial begin
        clk = 0;
        rst_n = 0;
        ena = 1;
        ui_in = 0;
        uio_in = 0;

        #20;
        rst_n = 1;

        ui_in[0] = 1;
        #100;

        ui_in[0] = 0;
        #100;

        $finish;
    end

endmodule

`default_nettype wire
