# -*- coding: utf-8 -*-
# Week 11, Homework
# Problem 1

"""
Incandescent light bulbs operate at a temperature of 2500 deg.C when bright and
2200 deg.C when dim. The creep rate of the filament when bright is 1.5 times that
when dim. Assuming that the activation energy is constant within this temperature
range, and that a single creep diffusion mechanism operates, calculate the
activation energy in kJ/mol. You can assume that the stress is the same when the
light is bright or dim. 
"""

import numpy as np
pi = np.pi

# Input data
TB = 2500.0 + 273.15
TD = 2200.0 + 273.15
ratio = 1.5

# Other necesary information
R = 8.314

# Determining the activation energy
coef = 1.0/(R*TD) - 1.0/(R*TB)
Q = np.log(ratio)/coef
print round(Q/1000.0,4), 'kJ/mol'