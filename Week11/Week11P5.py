# -*- coding: utf-8 -*-
# Week 11, Homework
# Problem 4

"""
Piping used in oil refineries usually experiences high pressures and temperatures
for extended periods of time, which as you all now know, leads to creep. In this
problem, we are going to try and predict the stress-rupture time of a S-590 alloy
steel pipe. We will use the Larson-Miller parameter which helps us predict the
lifetime of the material using the Arrhenius rate equation.
At a given stress, the L.M. parameter (in degrees Kelvin log[hours]) is given below:

L.M.parameter=T[log(tr)+C]

where T is temperature in Kelvin,
tr is stress-rupture time in hours
C is a material constant.

The following data are given for a S-590 steel pipe:
Operating Temperature (T): 550 deg.C
Inside Radius (r): 10cm
Thickness (t):  10mm
Axial length (l): 0.25m
Internal pressure: 40MPa
Materials Constant, C: 17log(hours)
"""

import numpy as np
pi = np.pi

# Input data
T = 550.0 + 273.15
r = 0.1
t = 0.01
l = 0.25
p = 40.0*1e6
R = 8.314

# Creating a function for the Larson-Miller parameter
def LMparam(Temp, hours):
    C = 17.0
    return Temp*(np.log10(hours) + C)

# Calculate the operating stress for this pipe
# (use the equation for hoop stress on a cylinder)
# assuming that you can approximate the pipe as a thin-walled cylinder.
Sh = p*r/t
#print round(Sh/1e6,4), 'MPa'

# Given that LMparam is about 17000, calculate the stress-rupture time in years
# Creating a function to determine time in years for a given LM param
def invLM(Temp,LMparam):
    C = 17.0
    exp = (LMparam/Temp)- C
    hours = 10.0**exp
    years = hours/(365.0*24.0)
    return years
print invLM(T,17013.139)