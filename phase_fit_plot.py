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
"""def correct_phase(x):
    if(x>0):
        if(x>90):
            return np.abs(x-180)
        else:
            return x
    else:
        return np.abs(x+180)
        """
def correct_phase_tweeter(x):
    if x>90:
        return np.abs(x-180)
    elif x<0:
        return np.abs(x)-180
    else:
        return x

def correct_phase_woofer(x):
    if x<0:
        return x+360
    else:
        return x
def deg_to_rad(x):
    return x*np.pi/180

correct_T = np.vectorize(correct_phase_tweeter)
correct_W = np.vectorize(correct_phase_woofer)
vect_deg_to_rad = np.vectorize(deg_to_rad)

#correct the phases
p_T=correct_T(p_T)
p_W=correct_W(p_W)

#Convert to radians
p_T=vect_deg_to_rad(p_T)
p_W=vect_deg_to_rad(p_W)

#Phase difference

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

plt.plot(f_T,p_T,
         color='blue',
         label='Tweeter')


plt.plot(f_W,p_W,
         color='orange',
         label='Woofer')


#Plot fits
plt.plot(f_T,ff.tweeter_phase(f_T,*T_fit),
         color='red',
         label='FIT_TWEETER')
#Plot fits
plt.plot(f_W,ff.woofer_phase(f_W,*T_fit),
         color='green',
         label='FIT_WOOFER')

plt.plot(f_W,ff.phase_difference(f_W,*W_fit,*T_fit),
         color='purple',
         label='Phase difference')

#Plot difference
#plt.plot(f_W-f_T)

#Graphics
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.xscale("log")
#plt.yscale("log")
plt.title("Crossover")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/phase_cross.png") # --> Per salvare
