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
r0 = 4.0 * b

# Determining shear modulus
G = 0.5*E/(1.0+nu)

# Determining the distance between dislocations
R = 1.0/np.sqrt(rho)

# Determining the strain energy per unit length of an edge dislocation
UE = G * b**2 * np.log(R/r0) / (4.0*pi*(1.0-nu))
print UE


"""
What is the exact strain energy per unit length of an screw dislocation for a
material that has a Young's modulus E of 50GPa, a Burger's vector b of 0.25nm,
a dislocation density ρ of 10^8cm−2, and a Poisson's ratio ν of 0.3?

Uscrew (in J/m)
"""
# Determining the strain energy per unit length of an screw dislocation
US = G * b**2 * np.log(R/r0) / (4.0*pi)
print US