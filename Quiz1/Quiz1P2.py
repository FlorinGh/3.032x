# -*- coding: utf-8 -*-
# Quiz 1

# Problem 2
# Aluminum is a cubic crystal, with
# S11 = 1.59×1e−11 m2/N
# S12 = −0.58×1e−11 m2/N
# S44 = 3.52×1e−11 m2/N

# Input data
S11 = 1.59*1e-11
S12 = -0.58*1e-11
S44 = 3.52*1e-11

# Part A: Determine E, nu and G
E = 1.0/S11
nu = -1.*S12*E
G = 1.0/S44
ansA = [round(E*1e-9, 5), round(nu, 5), round(G*1e-9, 5)]
print ansA

# Part B: For a single crystal of aluminum, loaded uniaxially along the crystal
# axis with a stress of σ1=10MPa, what are all of the components of strain?
s1 = 1.0*1e7
s2 = s3 = s4 = s5 = s6 = 0
e1 = S11*s1
e2 = S12*s1
e3 = S12*s1
e4 = e5 = e6 = 0
ansB = [round(e1,5),round(e2,5),round(e3,5),round(e4,5),round(e5,5),round(e6,5)]
print ansB

# Part C: What is the total elastic strain energy, per unit volume,
# for the uniaxial stress of 10MPa?
U = 0.5*(s1*e1+s2*e2+s3*e3+s4*e4+s5*e5+s6*e6)
print round(U, 5)