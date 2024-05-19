import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c
import uncertainty as uc

#Define values
L=c.Inductance
C=1.06e-6 #use initially detected capacity

Delta_L=0.01*L
Delta_C=0.01*C

#Evalueate cross frequency
fc=ff.fcross(L,C)

Delta_fc=uc.fcross(L,Delta_L,C, Delta_C)

print("Cross: {} +/- {}".format(fc,Delta_fc))