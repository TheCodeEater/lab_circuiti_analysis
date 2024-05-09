import numpy as np


filename = "data/misura errore.txt"
freq, amplitude, phase = np.loadtxt(filename, unpack=True)


#Compute sigma
A_sigma=np.std(amplitude)
F_sigma=np.std(freq)
P_sigma=np.std(phase)

print("Sigma ampiezza: {}".format(A_sigma))
print("Sigma frequenza: {}".format(F_sigma))