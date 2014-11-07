# Quiz 2, Problem 3

# Input data: time, stress and creep compliance
t = [0.0, 25.0, 50.0, 75.0]
s = [10.0, 30.0, 0.0, 0.0]
J = [1.0*1e-3, 1.4*1e-3, 1.6*1e-3, 1.7*1e-3]

# Determining the strain at 75 hours
e75 = s[0]*J[3] + (s[1]-s[0])*J[2] + (s[2]-s[1])*J[1]

# Printing the solution
print round(e75, 5)