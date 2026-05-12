`default_nettype none
`timescale 1ns / 1ps

module tb ();

  // VCD dump (for GTKWave)
  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
  end

  // Signals
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif

  // DUT: Up/Down Counter
  tt_um_example user_project (

`ifdef GL_TEST
      .VPWR(VPWR),
      .VGND(VGND),
`endif

      .ui_in  (ui_in),
      .uo_out (uo_out),
      .uio_in (uio_in),
      .uio_out(uio_out),
      .uio_oe (uio_oe),
      .ena    (ena),
      .clk    (clk),
      .rst_n  (rst_n)
  );

  // Clock generator (10ns period)
  always #5 clk = ~clk;

  // Stimulus
  initial begin
    clk = 0;
    rst_n = 0;
    ena = 1;
    ui_in = 0;
    uio_in = 0;

    #20;
    rst_n = 1;

    // Count UP
    ui_in[0] = 1;
    #100;

    // Count DOWN
    ui_in[0] = 0;
    #100;

    // Switch direction again
    ui_in[0] = 1;
    #100;

    $finish;
  end

endmodule
