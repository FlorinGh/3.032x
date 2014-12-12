# -*- coding: utf-8 -*-
# Quiz 3
# Problem 1

"""
The principal stresses acting on an aluminum component,
with a yield stress of 240MPa, are
σ=⎡⎣150    0  0
      0 −100  0
      0    0  125

"""

# Importing libraries
import numpy as np
pi = np.pi

# Input data
sy = 240.0
s1 = 150.0
s2 = 125.0
s3 = -100.0

"""
Calculate the difference between the maximum and minimum principal stresses.
Does the component fail according to the Tresca criterion?
"""
t = s1 - s3
print 'Tangetial stress is ', t

if t > sy:
    print 'The part will fail according to Tresca criterion'
else:
    print 'The part will pass the Tresca criterion'

"""
Calculate the equivalent stress.
Does the component fail according to the von Mises criterion?
"""
seq = np.sqrt(s1*s1 + s2*s2 + s3*s3 - s1*s2 - s2*s3 - s3*s1)
print 'Equivalent stress is ', round(seq,2)

if seq > sy:
    print 'The part will fail according to von Mises criterion'
else:
    print 'The part will pass the von Mises criterion'