# Week 5
# Problem 2

# Importing libraries
import numpy as np
pi = np.pi

# Input data
theta = pi/4.0
#stress = [10.0, 0.0, 0.0]
stress = [-11.0, 1.0, 8.0]
sx = stress[0]
sy = stress[1]
txy = stress[2]

# Determining the stress components for pi/4 CCW rotation
sx1 = 0.5*(sx+sy) + 0.5*(sx-sy)*np.cos(2.0*theta) + txy*np.sin(2.0*theta)
sy1 = 0.5*(sx+sy) - 0.5*(sx-sy)*np.cos(2.0*theta) - txy*np.sin(2.0*theta)
tx1y1 = 0.0 - 0.5*(sx-sy)*np.sin(2.0*theta) + txy*np.cos(2.0*theta)
ansA = [round(sx1,2), round(sy1,2), round(tx1y1,2)]
print ansA

# Determining the principal stress components and maximum shear
smed = 0.5*(sx+sy)
tmax = R = np.sqrt((0.5*(sx-sy))**2+(txy)**2)
s1 = smed + R
s2 = smed - R
ansB = [round(s1,2), round(s2,2), round(tmax,2)]
print ansB

# Determining the angle of rotation from sx to s1
alpha = pi + np.arctan(2*txy/(sx-sy))
ansC = round(0.5*180.0*alpha/pi, 2)
print ansC