# -*- coding: utf-8 -*-
# Week 10, Homework
# Problem 2

"""
What is the exact strain energy per unit length of an edge dislocation for a
material that has a Young's modulus E of 50GPa, a Burger's vector b of 0.25nm,
a dislocation density ρ of 10^8cm−2, and a Poisson's ratio ν of 0.3?

Uedge (in J/m)
"""

import numpy as np
pi = np.pi

b = 0.25*1e-9
E = 50.0*1e9
nu = 0.3
rho = 1.0*1e12

# Determining shear modulus
G = 0.5*E/(1+nu)

# Determining the line tension
T = 0.5*G*b**2

# Determining dislocation core radius
r = np.sqrt(1.0/rho)

"""
What is the exact strain energy per unit length of an screw dislocation for a
material that has a Young's modulus E of 50GPa, a Burger's vector b of 0.25nm,
a dislocation density ρ of 10^8cm−2, and a Poisson's ratio ν of 0.3?

Uscrew (in J/m)
"""