/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_updowncounter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // always 1 when powered
    input  wire       clk,      // clock
    input  wire       rst_n     // active-low reset
);

  reg [7:0] count;

  // Up/Down counter
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      count <= 8'b0;
    else if (ena) begin
      if (ui_in[0])
        count <= count + 1'b1;  // UP
      else
        count <= count - 1'b1;  // DOWN
    end
  end

  assign uo_out  = count;

  // Unused IOs
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // Prevent unused warnings
  wire _unused = &{ui_in[7:1], uio_in, 1'b0};

endmodule
