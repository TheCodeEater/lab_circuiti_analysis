import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c

x, p_W = np.loadtxt("data/phase_channels/woofer_phase.txt", unpack=True)

#Plot fits
plt.plot(x,ff.tweeter_phase(x,c.Capacitance),
         color='red',
         label='TWEETER')
#Plot fits
plt.plot(x,ff.woofer_phase(x,c.Inductance),
         color='green',
         label='WOOFER')

plt.plot(x,ff.phase_difference(x,c.Inductance,c.Capacitance),
         color='purple',
         label='Phase difference')

#Graphics
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.xscale("log")
#plt.yscale("log")
plt.title("Crossover")
#plt.show() # --> Per visualizzare
plt.savefig("./artifacts/phase_theoretical.png") # --> Per salvare