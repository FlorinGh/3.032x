# -*- coding: utf-8 -*-
# Week 12, Problem2

"""
A component is subjected to a tensile stress of 200MPa and the material that
the component is made of has a fracture toughness, KIC, of 35 MPam.
Calculate the length for the crack to cause failure if:
Part a: for an edge crack, with Y=1.12
Part b: for an internal crack, with Y=1.00
"""

# Input data
s = 200.0 * 1e6
KIC = 35.0 * 1e6
y1 = 1.12
y2 = 1.00

# Importing modules
import numpy as np

# Computing the total length for the crack to cause failure
KI = KIC
a1 = (1.0/np.pi) * (KI/y1/s)**2
print(a1*1e3)

a2 = 2.0 * (1.0/np.pi) * (KI/y2/s)**2
print(a2*1e3)

