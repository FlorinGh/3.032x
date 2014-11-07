# Quiz 2, Problem 6
import numpy as np

# Maxwell element
Em = 1.0*1e9
etam = 100.0*1e9

# Voigt element
Ev = 0.5*1e9
etav = 50.0*1e9

# The load
s1 = 10.0*1e6
s2 = -10.0*1e6
t1 = 0.0
t2 = 250.0
t3 = 500

# The compliance function
def J(t):
    # Maxwell element
    Em = 1.0*1e9
    etam = 100.0*1e9

    # Voigt element
    Ev = 0.5*1e9
    etav = 50.0*1e9
    
    # Maxwell compliance function
    Jm = 1.0/Em + t/etam
    
    # Voigt compliance function
    Jv = 1.0/Ev - (1.0/Ev)*np.exp(-Ev*t/etav)
    
    # The equivalent compliance function
    return Jm + Jv

e0 = s1*J(t1)
print round(e0, 4)

e250 = s1*J(t2-t1)
print round(e250, 4)

e500minus = s1*J(t3-t1)
print round(e500minus, 4)

e500plus = s1*J(t3-t1) + s2*J(t1)
print round(e500plus, 4)
