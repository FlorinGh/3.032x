# Quiz 1

# Problem 3


import numpy as np
sy = 220.0
KIC = 140.0
pi =  np.pi
a = 5.0*1e-3

rp = 1.0/(3.0*pi) * (KIC/sy)**2
print rp/a
if rp/a <0.02:
    print 'Griffith is valid'
else:
    print 'Grifith not valid'
