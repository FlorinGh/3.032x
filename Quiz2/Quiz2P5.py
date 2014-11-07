# -*- coding: utf-8 -*-
# Quiz 2, Problem 5
'''
Calculate the load that a fibroblast cell applies to buckle a single column in a
collagen tissue engineering scaffold, given that the column has a length of 100μm,
is circular in cross section, with a diameter of 2μm, and has a Young's modulus
of 5MPa. You can assume that the end constraint factor, n, for the column, is 0.6.
'''

import numpy as np
pi = np.pi

# Input data
L = 100.0*1e-6
D = 2.0*1e-6
E = 5.0*1e6
n = 0.6

# Geometric properties of the section
I = 0.25*pi*(D/2)**4

# Critical load for buckling
P = n**2*pi**2*E*I/L**2
print round(P*1e9, 4)