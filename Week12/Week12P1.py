# -*- coding: utf-8 -*-
# Week 12, Problem1

"""
While doing a routine check on several components, you find a 4mm long interior
crack, perpendicular to the applied tensile stress of 85 MPa on a part made of
a steel alloy that has a fracture toughness of 55 MPam. 
The geometrical factor for this crack is, Y=1.0.  

On another component made of a titanium alloy with a fracture toughness of 70 MPam
you find a 3mm long exterior crack on the edge of the component, perpendicular
to the tensile stress of 92 MPa.  The geometrical factor for this crack is Y=1.12.

For both components, you are required to have a factor of safety of 3,
meaning that if KI>KIC/3, then the component is considered to be unsafe
and is taken out of commission and replaced.
"""

# Input data
a1 = 2.0 * 1e-3
s1 = 85.0 * 1e6
KIC1 = 55.0 * 1e6
y1 = 1.0

a2 = 3.0 * 1e-3
s2 = 92.0 * 1e6
KIC2 = 70.0 * 1e6
y2 = 1.12

f = 3.0

"""
Calculate the stress intensity factor for both components
and determine if the components need to be replaced.
"""

# Importing modules
import numpy as np

# Computing the stress intensity factor for the two components
KI1 = y1 * s1 * np.sqrt(np.pi * a1)
print(round(KI1/1e6,2))

KI2 = y2 * s2 * np.sqrt(np.pi * a2)
print(round(KI2/1e6,2))

# What component needs to be replaced?
if KI1 > KIC1/f:
    print('The steel component must be replaced')
else:
    print('The steel component is good')

if KI2 > KIC2/f:
    print('The titanium component must be replaced')
else:
    print('The titanium component is good')

"""
For the steel component, determine the number of cycles of fatigue load that
it can withstand before it must be replaced. Assume that the minimum load for
each cycle is zero and the maximum is the same as in Part (a).
The Paris law for the steel component is:
da/dN = 1.0*1e-11*(dK)**3
"""

# New input data
dK = KI1
m = 3.0
A = 1.0 * 1e-11

# Determining the final crack length
KIf = KIC1 / f
af =(1.0/np.pi)*(KIf/(y1*s1))**2
print(round(af*1000,2))

# Determining the cycles to fatigue load before replacement
Nf = (-2.0/np.sqrt(af) + 2.0/np.sqrt(a1))/(A * (y1*s1*1e-6*np.pi**0.5)**m)
print(Nf)









