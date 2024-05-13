import sympy as sy
import fit_functions as ff

#Define symbols
dL, dC= sy.symbols("dL dC")

#Define uncerainty propagation
fcross_exp=sy.sqrt((sy.diff(ff.fcross_exp,ff.L)*dL)**2+(sy.diff(ff.fcross_exp,ff.C)*dC)**2)


#Create lambdas

#Accepts first L, dL, C, dC
fcross=sy.lambdify([ff.L,dL,ff.C,dC],fcross_exp)