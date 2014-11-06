#Quiz 2, Problem 2

# Importing libraries
import numpy as np
pi = np.pi

# The stress matrix for initial orientation of the element
# sx is the unknown
# we will create a function to look for the sx
sy = 8
txy = 16
s0 = 40

# Creating a function to determine the principal stress components
def S1(sx, sy = 8, txy = 16):
    smed = 0.5*(sx+sy)
    R = np.sqrt((0.5*(sx-sy))**2+(txy)**2)
    s1 = smed + R
    return s1

# Creating a search function for sx using bisection method
def searchSx(s):
    s0 = 40.0
    eps = 0.01
    if S1(s) > s0-eps and S1(s) < s0+eps:
        print 'Sx is ' + str(s)
    elif S1(s) < s0-eps:
        #print str(s) + ' is small'
        s = s + 0.1
        searchSx(s)
    else:
        #print str(s) + ' is big'
        s = s - 0.1
        searchSx(s)
        
searchSx(40)