# -*- coding: utf-8 -*-
# Week 12, Problem3

"""
A component, made from a material with a fracture toughness, KIC, of 50 MPam,
is exposed to a uniaxial tensile stress of 300MPa. During a routine inspection,
an edge crack of length 1 mm is discovered.
The geometrical factor, Y, for this crack is Y=1.12.
"""

# Input data
s = 300.0 * 1e6
KIC = 50.0 * 1e6
a = 1.0 * 1e-3
y = 1.12

# Importing modules
import numpy as np

# What is the stress intensity factor for this crack?
KI = y * s * np.sqrt(np.pi*a)
print(KI/1e6)

"""
If the stress is cycled between 0MPa and 300MPa in fatigue,
and the material obeys a Paris law, with da/dN=4.2*1e−10*(dK)**3,
how many cycles can the component withstand before fatigue failure?
"""

# New input data
m = 3.0
A = 4.2 * 1e-10

# Determining the final crack length
KIf = KIC
af =(1.0/np.pi)*(KIf/(y*s))**2
print(af*1000)

# Determining the cycles to fatigue load before replacement
dK = y * s * np.sqrt(np.pi*a)
Nf = (-2.0/np.sqrt(af) + 2.0/np.sqrt(a))/(A * (y*s*1e-6*np.pi**0.5)**m)
print(Nf)
