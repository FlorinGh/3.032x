# -*- coding: utf-8 -*-
# Week 11, Homework
# Problem 4

"""
A specimen has an initial diameter of 200mm and a length of 700mm.
At a stress of 40MPa and a temperature of 538 deg.C the steady state strain rate
is about 2*1e−4 % per hour. Find the primary creep elongation and the steady state
creep elongation after 5000 hours given that the creep deformation at that time is 7.2mm
"""

import numpy as np
pi = np.pi

# Input data
Diameter = 200.0*1e-3
Length = 700.0*1e-3
Stress= 40.0*1e6
Temperature = 538.0 + 273.15
epsSRate = 2.0*1e-6 / 3600.0
time = 5000*3600.0
deltaCreep = 7.2*1e-3

# Other necesary information
R = 8.314

# Determining the steady state creep elongation
epsS = epsSRate * time
elongationS = Length * epsS
print round(elongationS*1000.0,4), 'mm'

# Determining the primary creep elongation
elongationP = deltaCreep - elongationS
print round(elongationP*1000.0,4), 'mm'