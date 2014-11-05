# -*- coding: utf-8 -*-
# Quiz 1

# Problem set 6: A cube of the isotropic, linear elastic epoxy resin E=2GPa,
# nu=0.3, alpha=50×1e-6 at 20∘C is unloaded. It is then heated to 60∘C.

# What is the corresponding strain matrix?

# Input data
E = 2.0*1e9
nu = 0.3
alpha = 50*1e-6
T = 40

# Computing the thermal strains
ex = ey = ez = alpha*T
eyz = exz = exy = 0
ans = [ex, ey, ez, eyz, exz, exy]
print ans

# The temperature is held constant at 60∘C. What stress is required to reduce
# all the components of the strain matrix to zero?
# Computing the thermal stress
# normal stress on all directions acts in the same time
s = 1e-6*ex*E/(1.0-2.0*nu)
print round(s,5)