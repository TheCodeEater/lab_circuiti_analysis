import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c
import uncertainty as uc
import sympy as sy

#compute y equiv error

#create delta symbols
df=sy.symbols("df")

#Phase equiv error
#gives y-interval as function of x-interval
phase=sy.diff(ff.p_diff,ff.f)*df
phase=phase.subs(df,0.001).subs(ff.L,0.0114672).subs(ff.C,1.0036805e-6) #use average value

phase_sigma_eq=sy.lambdify([ff.f],phase)

#print(phase_sigma_eq(1000))

phase_sigmaeq_vec=np.vectorize(phase_sigma_eq)