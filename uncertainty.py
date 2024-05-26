import sympy as sy
import fit_functions as ff
import numpy as np

#Define symbols
dL, dC, dV, dVin, Vin= sy.symbols("dL dC dV dVin Vin")

#Define uncerainty propagation
fcross_exp=sy.sqrt((sy.diff(ff.fcross_exp,ff.L)*dL)**2+(sy.diff(ff.fcross_exp,ff.C)*dC)**2)

#Gain uc
gain_uc=sy.sqrt((dV/Vin)**2+ff.V*(dVin/Vin)**2)


#Create lambdas

#Accepts first L, dL, C, dC
fcross=sy.lambdify([ff.L,dL,ff.C,dC],fcross_exp)
gain=sy.lambdify([ff.V,Vin,dV,dVin],gain_uc)

gain_vec=np.vectorize(gain)