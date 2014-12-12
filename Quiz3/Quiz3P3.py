# Quiz 1
# Problem 3

"""
Two single edge notch specimens, one made of cast iron and the other of mild steel,
each with a semi-crack length, a, of 5mm, are loaded in tension. 
The yield strength and fracture toughness of the materials are listed below.
cast iron: 450 / 10
mild steel: 220 / 140
"""
# Importing modules
import numpy as np
pi = np.pi

# Input data
a = 5.0*1e-3
Y = 1.12

sy1 = 450.0
KIC1 = 10.0
sy2 = 220.0
KIC2 = 140.0

"""
Assuming that linear elastic fracture mechanics applies, calculate the stress
required for fracture according to the Griffith criterion for each material.
The geometrical factore Y for the stress intensity factor in such specimens is 1.12.
"""
s1 = KIC1/(Y*np.sqrt(pi*a))
print 'Cast iron fractures at ', round(s1,2), ' MPa'
s2 = KIC2/(Y*np.sqrt(pi*a))
print 'Mild steel fractures at ', round(s2,2), ' MPa'

"""
For which of the materials is the Griffith criterion valid at fracture,
assuming plane strain conditions at the crack tip?
"""
rp1 = 1.0/(3.0*pi) * (KIC1/sy1)**2
rp2 = 1.0/(3.0*pi) * (KIC2/sy2)**2
if rp1/a <0.02:
    print 'Griffith criterion is valid for cast iron'
else:
    print 'Grifith criterion is not valid for cast iron'
if rp2/a <0.02:
    print 'Griffith criterion is valid for mild steel'
else:
    print 'Grifith criterion is not valid for mild steel'