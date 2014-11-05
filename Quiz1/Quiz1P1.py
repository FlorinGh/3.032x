# -*- coding: utf-8 -*-
# Quiz 1

# Problem 1
# A cylindrical pressure vessel, with a diameter of 40cm and a wall thickness of
# 10mm is made of steel (isotropic, with Young’s modulus = 200GPa; Poisson’s 
# ratio = 0.28) and is pressurized to 20MPa. The longitudinal and hoop stresses 
# in the wall, σl and σh, respectively, are given by:
# σl=pr/2t and σh=pr/t
#What is the strain in the radial direction,
# through the thickness of the pressure vessel?

# Input data
D = 0.4
t = 0.01
E = 200.0*1e9
nu = 0.28
p = 20.0*1e6

# Computing the stresses
r = D/2.0
sl = (p*r)/(2*t)
sh = (p*r)/t
sr = 0 # this value is insignificant

# Solving analitically
er = sr/E - nu*sl/E - nu*sh/E

# Printing the result
print round(er, 5)