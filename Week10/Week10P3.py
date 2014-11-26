# -*- coding: utf-8 -*-
# Week 10, Homework
# Problem 3
"""
Consider a sample of well-annealed copper. Find the Burger's vector given that
the energy per unit line length is 1.4×10^−9J/m, E=177GPa and nu=0.36.
Assume alpha=0.5.
"""
import math as mth

# Input data
E = 177.0*1e9
nu = 0.36
Uel = 1.4*1e-9
alpha = 0.5

# Determining the shear modulus
G = 0.5*E/(1.0 + nu)

# Determining Burgers vector
b = mth.sqrt(Uel/(alpha*G))

print round(b*1e9, 5), 'nm'