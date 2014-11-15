# -*- coding: utf-8 -*-
# Week 9, Homework

import numpy as np

# Problem 2
"""
Determine the stress to cause yielding using Von Mises criteria for the system
σx=20MPa,σy=10MPa, and τxy=3MPa. Use the following two different approaches.
First determine the equivalent stress using the given data.
Second, calculate the principal stresses and use that values to determine
the equivalent stress.
"""

# Input data (the complete stress matrix)
Sx = 20.0
Sy = 10.0
Sz = 0.0
Sxy = 3.0
Syz = 0.0
Szx = 0.0

# Computing the von Mises equivalent stress using the components of stress
Seq1 = np.sqrt(0.5*((Sx-Sy)**2 + (Sy-Sz)**2 + (Sz-Sx)**2) + 3*Sxy**2 + 3*Syz**2 + 3*Szx**2)
print 'Seq1 is ' + str(round(Seq1,4))

# Computing the equivalent stress using principal stress components
Smed = 0.5*(Sx + Sy)
R = np.sqrt((0.5*Sx - 0.5*Sy)**2 + Sxy**2)
S1 = Smed + R
print 'S1 is ' + str(round(S1,4))
S2 = Smed - R
print 'S2 is ' + str(round(S2,4))
S3 = 0.0
Seq2 = np.sqrt(S1**2 + S2**2 + S3**2 - S1*S2 - S2*S3 - S3*S1)
print 'Seq2 is ' + str(round(Seq2,4))
