How it works
This is an 8-bit up/down counter. On every rising clock edge:
ui[0] = 1 → count increases by 1
ui[0] = 0 → count decreases by 1
rst_n = 0 → counter resets to 0
Output uo[7:0] shows the current count (with wraparound at 0–255).

How to test
Set rst_n = 0, then 1 → output becomes 0
Set ui[0] = 1 → observe counting up
Set ui[0] = 0 → observe counting down
Check wraparound at 255 → 0 and 0 → 255
View uo[7:0] in simulation or LEDs

External hardware
None required.
Optional: connect uo[7:0] to LEDs to see the binary count.
