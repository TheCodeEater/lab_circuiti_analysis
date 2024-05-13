import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c
import uncertainty as uc

# Load phase data
f_T, p_T, pT_error = np.loadtxt("data/channels/dati", unpack=True,usecols=(0,7,8))
f_W, p_W, pW_error = np.loadtxt("data/channels/dati", unpack=True,usecols=(0,5,6))

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

    if(x>np.pi/2):
        y= x-np.pi
    else:
        y=x

    if(y<0):
        return y+np.pi
    else:
        return y

def correct_phase_woofer(x):
    y = x - np.pi
    if (y > np.pi / 2):
        return y - np.pi
    else:
        return y

def rad2deg(x):
    return x*180/np.pi


def correct_phase(x):
    return x%360

correct_T = np.vectorize(correct_phase_tweeter)
correct_W = np.vectorize(correct_phase_woofer)
vect_rad2deg = np.vectorize(rad2deg)

#correct the phases
p_T=correct_T(p_T)
p_W=correct_W(p_W)

#Systematic error correction
def correct_systematic_1(p,f):
    return p+2*np.pi*f*c.T_delay

def correct_systematic_2(p,f):
    return p - 2 * np.pi * f * 2*c.T_delay

#Systematic correction
p_T=correct_systematic_1(p_T,f_T)

#Convert to degress
#p_T=vect_rad2deg(p_T)
#p_W=vect_rad2deg(p_W)

#Phase difference
#p_W=correct_systematic_2(p_W,f_W)

#Systematic oscillation correction
p_T=p_T-p_W


# Perform fit
"""
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
                          """
Diff_fit, pcov_diff = sp.curve_fit(ff.phase_difference,
                                   xdata=f_T,
                                   ydata=p_T,
                                   sigma=pT_error,
                                   p0=[c.Inductance,c.Capacitance,0],
                                   bounds=[[0,0,-20],[1.5e-2,1e-5,20]])

# Plot

plt.plot(f_T,p_T,
         color='blue',
         label='Tweeter')


plt.plot(f_W,p_W,
         color='orange',
         label='Woofer')

plt.plot(f_T,ff.phase_difference(f_T,*Diff_fit),
         color='green',
         label='Fit')

#Better symbols
L=Diff_fit[0]
Delta_L=np.sqrt(pcov_diff[0][0])
C=Diff_fit[1]
Delta_C=np.sqrt(pcov_diff[1][1])
Offset=Diff_fit[2]
Delta_offset=np.sqrt(pcov_diff[2][2])

#Write fit data
print("L: {} +/- {}\n".format(L,Delta_L))
print("C: {} +/- {}\n".format(C,Delta_C))
print("Offset: {} +/- {}\n".format(Offset,Delta_offset))

print("Fcross: {} +/- {}\n".format(1/(2*np.pi*np.sqrt(L*C)),uc.fcross(L,Delta_L,C,Delta_C)))

#Search for maximum phase displacement
max_index=np.argmax(p_T)
max_phase_diff=p_T[max_index]
max_pdiff_freq=f_T[max_index]

print("Maximum phase difference: {}\nAt frequency: {}".format(max_phase_diff,max_pdiff_freq))

#Plot fits
"""""
plt.plot(f_T,ff.tweeter_phase(f_T,*T_fit),
         color='red',
         label='FIT_TWEETER')
#Plot fits
plt.plot(f_W,ff.woofer_phase(f_W,*T_fit),
         color='green',
         label='FIT_WOOFER')

plt.plot(f_W,ff.phase_difference(f_W,*W_fit,*T_fit),
         color='purple',
         label='Phase difference')"""

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
