Project: to visualise G-codes used by CNC machines using python.

Aim is to trace the shape given by the G-code commands. Hence, I will skip over the Z axis line codes, and ignore the M-codes related to spindle movements and cutting.
The speed of the movements defined by G00 and G01 will be predefined and variable depending on user.

The G-codes taken into consideration are:
1. G00 --> rapid move from (x,y) to (x+x0, y+y0), may not be a straight line motion
2. G01 --> controlled move from (x,y) to (x+x0, y+y0), straight line motion
3. G02 --> clockwise curve
4. G03 --> anti-clockwise curve
5. G21 --> metric mode
6. G20 --> imperial mode 
7. G90 --> absolute distancing
8. G91 --> incremental distancing
9. G94 --> feed rate in inches/mm per min
10. G53 --> machine coordinates
11. G54 --> coordinate system 

The M-codes and letter codes taken into consideration are:
1. M0 --> pause machine
2. M2 --> end program
3. M30 --> end program and loop to first line
4. R --> radius in G02 and G03
5. X --> x coordinate specification
6. Y --> y coordinate specification
7. N --> line number
8. I --> radius specification for a circle

The libraries used in python are turtle and math. Note, for the code to run, you need the turtle library.
To install turtle use:

  $pip install turtle

on the command prompt, or linux terminal.
