# -*- coding: utf-8 -*-
# Quiz 1

# Problem set 4: A linear elastic, isotropic epoxy resin with elastic modulus,
# E=2GPa, and Poisson’s ratio, ν=0.3, is loaded by the following stress state
# (see the loading data below for loading matrix)
# Give numerical values for all strain components in the corresponding strain matrix.

# Importing libraries
import numpy as np

# Input data
E = 2.0*1e9
nu = 0.3
G = 0.5*E/(1+nu)

# Loading data
sx = 10*1e6
sy = -20*1e6
sz = 0
syz = 0
sxz = 0
sxy = 5*1e6

# Computing normal strains
S = np.array([[1.0,-1.0*nu,-1.0*nu],[-1.0*nu,1.0,-1.0*nu],[-1.0*nu,-1.0*nu,1.0]])
normal = sum((1/E)*S.T*np.array([[sx], [sy], [sz]]))
ex = normal[0]
ey = normal[1]
ez = normal[2]
print normal

# Computing shear strains
shear = (1/G)*np.array([[syz, sxz, sxy]])
eyz = shear[0,0]
exz = shear[0,1]
exy = shear[0,2]
print shear

# Computing elastic strain energy per unit volume
s = np.array([[sx], [sy], [sz], [syz], [sxz], [sxy]])
e = np.array([[ex],[ey], [ez], [eyz], [exz], [exy]])
U= 0.5*sum(s*e)
print U[0]