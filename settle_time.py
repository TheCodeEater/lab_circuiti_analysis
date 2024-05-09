import numpy as np
import matplotlib.pyplot as plt
import fit_functions as ff
import scipy.optimize as sp
import constants as c

f=21000
A=0.19


#load data
t_0, val_0, t_1, val_1=np.loadtxt("./data/multiplexer_phase/sfasamento multiplexer 21KHz", unpack=True)

#fit sinusoidal
# sinusoide con fase
def sin(t,p):
    return A*np.sin(2*np.pi*f*t+p)

P0_fit, pcov0 = sp.curve_fit(sin,
                             xdata=t_0,
                             ydata=val_0,
                             p0=[0])

P1_fit, pcov1 = sp.curve_fit(sin,
                             xdata=t_1,
                             ydata=val_1,
                             p0=[0.5])

plt.plot(t_0,val_0, label="AI0")
plt.plot(t_1,val_1, label="AI1")
plt.plot(t_0,sin(t_0,*P0_fit), label="Fit curva 0")
plt.plot(t_1,sin(t_1,*P1_fit), label="Fit curva 1")

print(P0_fit)
print(P1_fit)

plt.legend()

print("Fase 0: {}".format(P0_fit[0]))
print("Fase 1: {}".format(P1_fit[0]))
phase_diff=-P0_fit[0]+P1_fit[0]
print("Diff: {}".format(phase_diff))

time=phase_diff/(2*np.pi*f)

print("Time: {}".format(time))

plt.savefig("artifacts/settle_time.png")