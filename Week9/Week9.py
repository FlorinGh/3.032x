# Week 9, Homework

import numpy as np

# Problem 1
Sy = 400.0

# Rankine
szR = Sy

# Tresca
szT = Sy

# von Mises
szM = 2.0*Sy/np.sqrt((1.0-0.33)**2 + 2)
print szM

# What percent is the Von Mises result different from the Tresca result?
p = 100.0*szM/szT
print p