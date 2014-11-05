# Week 7

import numpy as np
pi = np.pi

# Problem 4
m = 1.0
E = 69.0*1e9
L = 0.5
t = 0.005
rho = 2700.0

r1 = np.sqrt(m/(rho*L*pi))
I1 = pi*r1**4/4.0
P1 = pi**2*E*I1/L**2
print P1/1000.0

r2 = (m + rho*L*pi*t**2)/(2*pi*rho*L*t)
I2 = (pi*r2**4 - pi*(r2-t)**4)/4.0
P2 = pi**2*E*I2/L**2
print P2/1000.0

# Problem 6
E = 193.0*1e9
nu = 0.29
r = 1.2*1e-2
t = 0.7*1e-3
L = 5.0*1e-2
n = 1.0

A = 2*pi*r*t
I = pi*(r**3)*t

Peu = (pi**2*E*I)/L**2

s_lo = E*t/(r*np.sqrt(3*(1-nu**2)))
Plo = A*s_lo

ans6 = [round(Peu/1000.0, 3), round(Plo/1000.0, 3)]
#print ans6

# Problem 7
Ep = 3.5*1e9
Rhop = 0.3

Ea = 72.0*1e9
Rhoa = 0.1
C1 = 1.0

EpF = C1*Ep*Rhop**2
EaF = C1*Ea*Rhoa**2
ans7 = [round(EpF/1e9,5),round(EaF/1e9,5)]
#print ans7

# Problem 8
Rho = 0.1
Es = 3.5*1e9
C2 = 0.05
eps = 0.85

sel = C2*Es*Rho**2

EF = C1*Es*Rho**2
el = sel/EF
U = 0.5*el*sel + sel*(eps-el)
ans8 = [round(sel/1e6,3), round(U/1e6,3)]
print ans8