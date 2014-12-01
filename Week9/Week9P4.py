# -*- coding: utf-8 -*-
# Week 9, Homework

import numpy as np

# Problem 4
"""
An aluminum alloy has a yield strangth σy=150MPa. A component made from this alloy
is subjected to σx=200MPa and σy=50MPa, with all other stresses equal to zero.
"""

# Input data (the complete stress matrix)
sx = 200.0
sy = 50.0
sz = 0.0
sxy = 0.0
syz = 0.0
szx = 0.0

Sy = 150.0


# Computing the principal stress components
smed = 0.5*(sx + sy)
R = np.sqrt((0.5*sx - 0.5*sy)**2 + sxy**2)
s1 = smed + R
print 's1 is ' + str(round(s1,4))
s2 = smed - R
print 's2 is ' + str(round(s2,4))
s3 = 0.0
print 's3 is ' + str(round(s3,4))

# Calculate the difference between the maximum and minimum principal stresses.
print (s1-s3)

# Does the component fail according to the Tresca criterion?
print (s1-s3) > Sy

# Calculate the equivalent stress using principal stress components
seq = np.sqrt(s1**2 + s2**2 + s3**2 - s1*s2 - s2*s3 - s3*s1)
print 'seq is ' + str(round(seq,4))

# Does the component fail according to the von Mises criterion?
print seq > Sy
