# -*- coding: utf-8 -*-
# Quiz 1

# Problem 3
# Rubber particles, roughly 1mm in diameter, have been added to an epoxy resin
# to increase its resistance to crack growth. Estimate the Young's modulus of
# the composite, given that the Young's moduli of the epoxy and the rubber are,
# respectively, 2GPa and 10MPa, and that the volume fraction of the rubber
# particles is 5%.

# Input data
Erub = 1.0*1e7
Eepo = 2.0*1e9
Vrub = 0.05
Vepo = 1.0 - Vrub

# Estimate the Young's modulus of the composite
E = (Erub*Eepo)/(Vrub*Eepo + Vepo*Erub)

print round(E*1e-9, 5)