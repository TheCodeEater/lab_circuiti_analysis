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
#Load also vin data
f_Vin, A_Vin, AVin_err=np.loadtxt("data/channels/vin",unpack=True,usecols=(0,1,2))


# Plotting
#Plot experimental points
plt.plot(f_T,A_T,
         color='blue',
         label='Tweeter')
plt.plot(f_W,A_W,
         color='orange',
         label='Woofer')

plt.plot(f_Vin,A_Vin,
         color='purple',
         label='Vin')



#Graphics
plt.legend()
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza (V)")
plt.xscale("log")
#plt.yscale("log")
plt.title("Risposta in frequenza - Dati sperimentali")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/cross_dataonly.png") # --> Per salvare