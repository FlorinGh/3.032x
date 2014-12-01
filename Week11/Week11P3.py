# -*- coding: utf-8 -*-
# Week 11, Homework
# Problem 3

"""
Steady state power law creep data for a steel alloy at 60MPa are given below.
strain rate = 1.0*1e-5 @ T = 977
strain rate = 2.5*1e-5 @ T = 1089
The stress exponent, n, for this alloy is 6.
Find the steady state strain rate at 1200K and 45MPa.
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