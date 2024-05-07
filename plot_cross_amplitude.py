import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c

# Data loading
f_T, A_T=np.loadtxt("data/channels/Misura tewwter sweep 2kpt-B 300kpt-s.txt", unpack=True)
f_W, A_W=np.loadtxt(
    "data/channels/Misura woofer sweep 200-19953Hz 2kp-B 300kpt-s.txt", unpack=True)

#Fit tweeter
#Initial parameters
sigma=1e-4

T_fit, pcov1 = sp.curve_fit(ff.tweeter_volt,
                          xdata= f_T,
                          ydata= A_T,
                          sigma=sigma,
                          p0=[c.Capacitance],
                          bounds=[0,100])

W_fit, pcov2 = sp.curve_fit(ff.woofer_volt,
                          xdata= f_W,
                          ydata= A_W,
                          sigma=sigma,
                          p0=[c.Inductance],
                          bounds=[0,100])

# Plotting
#Plot experimental points
plt.plot(f_T,A_T,
         color='blue',
         label='Tweeter')
plt.plot(f_W,A_W,
         color='orange',
         label='Woofer')

#Plot fits
plt.plot(f_T,ff.tweeter_volt(f_T,*T_fit),
         color='red',
         label='FIT_TWEETER')
#Plot fits
plt.plot(f_W,ff.woofer_volt(f_W,*W_fit),
         color='green',
         label='FIT_WOOFER')

#Graphics
plt.legend() 
plt.xlabel("x")
plt.ylabel("y")
plt.xscale("log")
#plt.yscale("log")
plt.title("Crossover")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/cross.png") # --> Per salvare