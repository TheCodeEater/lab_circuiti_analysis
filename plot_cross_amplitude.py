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

#Get maximum of vin
max_index=np.argmax(A_Vin)
max_vin=A_Vin[max_index]
max_vin_freq=f_Vin[max_index]

#Compute gain
A_T=A_T/A_Vin
A_W=A_W/A_Vin

AT_err=uc.gain_vec(A_T,A_Vin,AT_err,AVin_err)
AW_err=uc.gain_vec(A_W,A_Vin,AW_err,AVin_err)

#Compute uncerainty
AT_err=AT_err+0.002
AW_err=AW_err+0.002
#Fit tweeter


T_fit, pcovT, infoT , junk, junka= sp.curve_fit(ff.tweeter_gain,
                          xdata= f_T,
                          ydata= A_T,
                          sigma=AT_err,
                          p0=[c.Capacitance],
                          bounds=[0,100],
                        full_output=True)

W_fit, pcovW, infoW, junk1,junk2 = sp.curve_fit(ff.woofer_gain,
                          xdata= f_W,
                          ydata= A_W,
                          sigma=AW_err,
                          p0=[c.Inductance],
                          bounds=[0,100],
                                                full_output=True)

# Plotting
#Plot experimental points
plt.plot(f_T,A_T,
         color='blue',
         label='Tweeter')
plt.plot(f_W,A_W,
         color='orange',
         label='Woofer')
"""
plt.plot(f_Vin,A_Vin,
         color='purple',
         label='Vin')
         """

#Plot fits
plt.plot(f_T,ff.tweeter_gain(f_T,*T_fit),
         color='red',
         label='FIT_TWEETER')
#Plot fits
plt.plot(f_W,ff.woofer_gain(f_W,*W_fit),
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
print("Maximum Vin value: {}\n At frequency: {} +/- {}\n".format(max_vin,max_vin_freq,8))


#Compute chi square
residualsT=infoT["fvec"]
residualsW=infoW["fvec"]

chisqT=sum(residualsT**2)
chisqW=sum(residualsW**2)

#reduce
dof=385 #(values)
constraints=2 #L and C are extracted
dof=dof-constraints

print("ChiT: {}".format(chisqT/dof))
print("ChiW: {}".format(chisqW/dof))

#Graphics
plt.legend() 
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza (V)")
plt.xlim(1000,2000)
plt.xscale("log")
#plt.yscale("log")
#plt.title("Risposta in frequenza - Guadagno in tensione")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/cross.png") # --> Per salvare