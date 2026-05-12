`default_nettype none

module tt_um_updowncounter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

  reg [7:0] count;

  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      count <= 8'd0;              // ✅ proper reset
    else if (ena) begin
      if (ui_in[0])
        count <= count + 1'b1;    // UP
      else
        count <= count - 1'b1;    // DOWN
    end
  end

  assign uo_out  = count;
  assign uio_out = 8'd0;
  assign uio_oe  = 8'd0;

endmodule
