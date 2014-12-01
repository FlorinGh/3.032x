# -*- coding: utf-8 -*-
# Week 10, Homework
# Problem 1

"""
A material has a Young's modulus E of 50GPa, a Burger's vector b of 0.25nm, and 
a Poisson's ratio ν of 0.3.
What is the approximate line tension for a dislocation in this material?
Line tension (in N):
"""

import numpy as np
pi = np.pi

b = 0.25*1e-9
E = 50.0*1e9
nu = 0.3

# Determining shear modulus
G = 0.5*E/(1+nu)

# Determining the line tension
T = 0.5*G*b**2
print T, 'N'