import numpy as np

s1 = 10.0*1e6
s2 = 10.0*1e6
s3 = -20.0*1e6

def Jv(t):
    E = 200.0*1e6
    eta = 25000.0*1e6
    J = (1.0/E)*(1-np.exp(-E*t/eta))
    return J

ev50 = s1*Jv(50.0)
ev150 = s1*Jv(150.0) + s2*Jv(50.0)
ev300 = s1*Jv(300.0) + s2*Jv(200.0) + s3*Jv(100)

ansV = [round(ev50,4), round(ev150,4), round(ev300,4)]
print ansV

def Jm(t):
    E = 5000.0*1e6
    eta = 50000.0*1e6
    J = 1.0/E + t/eta
    return J

em50 = s1*Jm(50.0)
em150 = s1*Jm(150.0) + s2*Jm(50.0)
em300 = s1*Jm(300.0) + s2*Jm(200.0) + s3*Jm(100)

ansM = [round(em50,4), round(em150,4), round(em300,4)]
print ansM