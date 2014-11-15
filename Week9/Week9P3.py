# -*- coding: utf-8 -*-
# Week 9, Homework

import numpy as np

# Problem 3
"""
The lattice for calcium is FCC, and the radius, r, of a calcium atom is 197pm.
Assuming that the dislocation density ρ is 5×1e8 cm−2 and that it remains constant,
and the plastic shear strain rate γ˙ is 8×1e−5 s−1, what is the mean velocity of
the dislocation? Note that for an FCC crystal, the Burgers vector is equal to 2r.
"""

# Input data 
r = 197.0*1e-12
rho = 5.0*1e12
gama = 8.0*1e-5
b = 2*r

# Computing the velocity of dislocation
v = gama/(b*rho)
print 'Velocity dislocation is ' + str(v)

