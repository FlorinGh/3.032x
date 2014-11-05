# -*- coding: utf-8 -*-
# Quiz 1

# Problem set 5: An isotropic epoxy resin (E=2GPa, nu=0.3) is reinforced by 
# unidirectional glass fibers (Eglass=70GPa), aligned in the 2 direction,
# such that the fiber composite is transversely isotropic, with the 1-3 plane
# being the plane of isotropy. The elastic constants of the fiber composite are
# given below. 
# What is the volume fraction of fibers in the composite?

# Input data
Ep = 2.0
Es = 70.0

E1 = 3.3 # the lower boundary, transversaly loaded
E2 = 29.2 # the upper boundary, longitudinaly loaded

# Computing the solutions
V2 = (E2/Ep - Ep/E1)/(Es/Ep - Ep/Es)
print round(V2, 5)
