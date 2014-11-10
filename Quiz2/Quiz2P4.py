# -*- coding: utf-8 -*-
# Quiz 2, Problem 4
'''
The television coverage of the World Series showed several remarkable slow-motion
views of the deflection of the bat as it hit the ball. Major league wood baseball
bats are made of ash. A typical major league bat has a length of 0.95m and a
tapering circular cross section. The ball typically hits the bat 150mm from the
free end (see figure below). Occasionally, the bat breaks as it hits the ball.

For this problem, you can assume that the bat is a cylinder of constant radius and
that the batter holds the end of the bat rigidly, so that it is loaded as a
cantilever beam.
'''

# Input data
E = 10.0*1e9
sb = 100.0*1e6
L = 0.8
r = 22.0*1e-3

# The deflection formula
delta = (sb*L**2)/(3*E*r)
print round(delta*1e3, 5)
    