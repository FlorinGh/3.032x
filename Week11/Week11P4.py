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
S1 = 60.0*1e6
eps1 = 1.0*1e-5
T1 = 977.0
eps2 = 2.5*1e-3
T2 = 1089.0
S3 = 45.0*1e6
T3 = 1200.0

# Other necesary information
R = 8.314
n = 6
ratio = eps1/eps2

# Determining the activation energy
coef = 1.0/(R*T2) - 1.0/(R*T1)
Q = np.log(ratio)/coef
print round(Q/1000.0,4), 'kJ/mol'

# Determining eps3
r = ((S3/S1)**n)*np.exp(Q*(1/(R*T1) - 1/(R*T3)))
eps3 = r*eps1
print round(eps3, 4), 's^-1'