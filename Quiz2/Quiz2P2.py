# Quiz 2, Problem 3

# Input data
l = 200.0*1e-6
b = 20.0*1e-6
h = 1.0*1e-6
E = 300.0*1e9
emax = 0.1*1e-2

# Geometric properties of the beam
ymax = h/2.0
I = (b*h**3)/12.0

# Determining the maximum P
smax = E*emax
Mmax = smax*I/ymax
Pmax = Mmax/l

# Printing the solution, force in microN
print round(Pmax*1e6, 5)