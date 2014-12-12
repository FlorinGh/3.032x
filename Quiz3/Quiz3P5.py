# Quiz 3
# Problem 5

"""
An aluminum (KIC=15 MPam) thin-walled, cylindrical pressure vessel has a radius
of 0.25m and a wall thickness of 10mm. There is a penny shaped crack of length, 
2a=2mm, in the wall of the pressure vessel, oriented such that the length of the
crack is normal to the hoop stress.
Assuming that linear elastic fracture mechanics applies and that the geometrical
factor, Y, for calculating the stress intensity factor is equal to 2,
at what pressure does the vessel fracture?
"""

# Input data
KIC = 15.0
R = 0.25
t = 10.0*1e-3
a = 1.0*1e-3
Y = 2.0

# Importing modules
import numpy as np
pi = np.pi

"""At what pressure does the vessel fracture?"""
# Determining the fracture stress
sh = KIC/(Y*np.sqrt(pi*a))
print 'The vessel fractures at ', round(sh,2), ' MPa'

# What pressure is needed to develop this stress?
p = sh*t/R
print 'The pressure to develop this hoop stress is ', round(p,2), ' MPa'


