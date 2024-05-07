import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c

# Load phase data
f_T, p_T = np.loadtxt("data/phase_channels/tweeter_phase.txt", unpack=True)
f_W, p_W = np.loadtxt("data/phase_channels/woofer_phase.txt", unpack=True)

#Correct data
#If phase is negative
def correct_phase(x):
    if(x>0):
        return x
    else:
        return -x

correct_vector = np.vectorize(correct_phase)

#correct the phases
p_T=correct_vector(p_T)
p_W=correct_vector(p_W)

#Define phase uncertainty
sigma=1e-4

# Perform fit
T_fit, pcov1 = sp.curve_fit(ff.tweeter_phase,
                          xdata= f_T,
                          ydata= p_T,
                          sigma=sigma,
                          p0=[c.Capacitance])

W_fit, pcov2 = sp.curve_fit(ff.woofer_phase,
                          xdata= f_W,
                          ydata= p_W,
                          sigma=sigma,
                          p0=[c.Inductance],
                          bounds=[0,100])

# Plot