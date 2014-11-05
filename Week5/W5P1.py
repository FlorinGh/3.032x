# Week 5
# Problem 1

# Importing libraries
import numpy as np
pi = np.pi

# Input data
W = 1000.0
alpha = 35.0*pi/180.0
smax = 1.1*1e6
tmax = 0.5*1e6

# Determining the minimum values for b
b1 = np.sqrt(W*(1.0 + np.cos(2.0*alpha))/(2.0*smax))
b2 = np.sqrt(W*np.sin(2.0*alpha)/(2.0*tmax))
ans = 100.0*max(b1, b2)

print round(ans,3)