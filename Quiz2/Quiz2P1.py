# Quiz 2, Problem 1

# Importing libraries
import numpy as np
pi = np.pi

# The stress matrix for initial orientation of the element
stress = [-25.0, 10.0, 6.0]
sx = stress[0]
sy = stress[1]
txy = stress[2]

# Determining the principal stress components and maximum shear
smed = 0.5*(sx+sy)
tmax = R = np.sqrt((0.5*(sx-sy))**2+(txy)**2)
s1 = smed + R
s2 = smed - R

# Determining the angle of rotation from sx to s1
alpha = 0.5*(pi + np.arctan(2*txy/(sx-sy)))

# Printing the results for part A
print 'S1 is ' + str(round(s1,2)) + ' MPa'
print 'S2 is ' + str(round(s2,2)) + ' MPa'
print 'Tmax is ' + str(round(tmax,2)) + ' MPa'
print 'alpha is ' + str(round(alpha*180.0/pi,2)) + ' degrees'

# Determining the stress components for 50 deg CCW rotation
theta = 50.0*pi/180.0
sx1 = 0.5*(sx+sy) + 0.5*(sx-sy)*np.cos(2.0*theta) + txy*np.sin(2.0*theta)
sy1 = 0.5*(sx+sy) - 0.5*(sx-sy)*np.cos(2.0*theta) - txy*np.sin(2.0*theta)
tx1y1 = 0.0 - 0.5*(sx-sy)*np.sin(2.0*theta) + txy*np.cos(2.0*theta)

# Printing the results for part B
print 'Sx1 is ' + str(round(sx1,2)) + ' MPa'
print 'Sy1 is ' + str(round(sy1,2)) + ' MPa'
print 'Tx1y1 is ' + str(round(tx1y1,2)) + ' MPa'
