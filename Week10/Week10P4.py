# -*- coding: utf-8 -*-
# Week 10, Homework
# Problem 4
# An isotropic alloy contains 5% by volume of a precipitate of radius 10nm.
# Assume the primary metal is in a simple cubic arrangement. The alloy has a Young's
# modulus E=70GPa and a Poisson's ratio ν=0.35. If Γ=0.9J/m2 (the energy needed
# to cut through the precipitate lattice per unit surface area), and b=0.25nm,
# what is the precipitate spacing L in the alloy?

import numpy as np
import math as mth
pi = np.pi

f = 0.05
r = 10.0*1e-9
E = 70.0*1e9
nu = 0.35
gamma = 0.9
b= 0.25*1e-9

# How many particles are there in one cell?
n = 8.0

# What is the volume of one particle of precipitate?
v = (4.0/3.0)*pi*r**3

# How much of this volume is in the cell?
p = 1.0/8.0

# These 8.0 particles ocupy 5% from the volume of one cubic arrangement
# What is the volume of one arrangement?
V = 20.0 * n * v * p

# The arrangement is cubic; you have the volume...
# What is the length of one side?
L = mth.pow(V, float(1)/3)
print round(L*1e9,5), 'nm'

# What is the shear stress required to move a dislocation past the precipitates?
taup = 2*gamma/L
print round(taup/1e6,5), 'MPa'

# Instead of introducing a precipitate into the primary metal, alumina,
# a dispersion compound is introduced.
# Consider the dislocation shown below, which bows to a radius of curvature R at
# an angle θ between two particles a distance L apart. Use the expression for line
# tension in a dislocation, the geometry of the bowing dislocation, and the force
# resulting from the applied shear stress to obtain an expression relating the
# applied shear stress and dislocation radius R. Express your answer in terms of
# the shear modulus G, the Burgers vector b, and the dislocation radius R.
# Hint: Draw the free body diagram for one of the particles.
# The force exerted by the stress on the dislocation is F=τbL

# Equilibrium:
# 2*T*sin(theta) = tau * b * L
# But
# T = 0.5 * G * B**2
# L = 2 * R * sin(theta)
# Then
# tau = (G * b) / (2 * R)
