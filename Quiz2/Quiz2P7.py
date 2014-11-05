# Quiz 2, Problem 7 
Rho = 0.1
Es = 1.5*1e9
C1 = 1.0
C2 = 0.05
eps = 0.80

Sel = C2*Es*Rho**2
Efoam = C1*Es*Rho**2

Eel = Sel/Efoam

U = 0.5*Eel*Sel + Sel*(eps-Eel)
print U