The provided G-code strings are 'cleaned' according to the specifications mentioned in the main README file. 
Changes made to the G-code are:
1. Remove Z paramters
2. Skip non-relevant M-codes
3. Format the code

This is done to make it easier to work with in python.

Example of a 'cleaned' G-code is:

From this:
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
G0X0.8276Y3.8621
G1Z0.1
G1X0.8276Y-1.9310
G0Z0.1
G0X1.1034Y3.8621
G0Z0.1
G0X1.1034Y3.0345
G1Z0.1

To this:
[
(G21, G90, G64 P0.003),
(G0, X0.8276, Y3.8621),
(G1, X0.8276, Y-1.9310),
(G0, X1.1034, Y3.0345)
]
