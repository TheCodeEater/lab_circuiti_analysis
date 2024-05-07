import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c

# Load phase data
f_T, p_T = np.loadtxt("data/phase_channels/tweeter_phase.txt", unpack=True)
f_W, p_W = np.loadtxt("data/phase_channels/woofer_phase.txt", unpack=True)

# Perform fit

# Plot