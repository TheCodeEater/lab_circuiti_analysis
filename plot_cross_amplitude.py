import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c
import uncertainty as uc

# Data loading
f_T, A_T, AT_err=np.loadtxt("data/channels/dati", unpack=True, usecols=(0,3,4))
f_W, A_W, AW_err=np.loadtxt(
    "data/channels/dati", unpack=True,usecols=(0,1,2))

#Fit tweeter
#Initial parameters
#sigma=1e-4

T_fit, pcovT = sp.curve_fit(ff.tweeter_volt,
                          xdata= f_T,
                          ydata= A_T,
                          sigma=AT_err,
                          p0=[c.Capacitance],
                          bounds=[0,100])

W_fit, pcovW = sp.curve_fit(ff.woofer_volt,
                          xdata= f_W,
                          ydata= A_W,
                          sigma=AW_err,
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

####
#Fit parameters
####
L=W_fit[0]
Delta_L=np.sqrt(pcovW[0][0])
C=T_fit[0]
Delta_C=np.sqrt(pcovT[0][0])

#Parameters itself
print("L: {} +/- {}\n".format(L,Delta_L))
print("C: {} +/- {}\n".format(C,Delta_C))

print("F Cross: {} +/- {}\n".format(ff.fcross(W_fit[0],T_fit[0]),uc.fcross(L,Delta_L,C,Delta_C)))

#print("C: {}\nL:{}\nfcross:{}".format(T_fit[0],W_fit[0],1/()))

#Graphics
plt.legend() 
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza (V)")
plt.xscale("log")
#plt.yscale("log")
plt.title("Ampiezza vs Frequenza - Dati sperimentali e fit")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/cross.png") # --> Per salvare