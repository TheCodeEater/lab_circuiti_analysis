#
# Define functions to be fit here
#
import sympy as sy
import constants as c
#Define symbols
# Resistance
# Input voltage
# Angular frequency
# Frequency
# Inductance
# Capacitance
R, V, w, f, L, C = sy.symbols("R V w f L C")

# Define voltage functions

#with pulsation
# Tweeter
woofer_exp = R*V/sy.sqrt(R**2+(w*L)**2)
#Woofer
tweeter_exp = R*V/sy.sqrt(R**2+(w*C)**-2)

#Conversion
# Frequency to angular frequency
f_conv = 2*sy.pi*f

#Switch to frequency and add parameters
tweeter_exp=tweeter_exp.subs(R,c.Res1).subs(V,c.Vin).subs(w,f_conv)
woofer_exp=woofer_exp.subs(R,c.Res2).subs(V,c.Vin).subs(w,f_conv)


#Create lambdas
woofer_volt = sy.lambdify([f, L], woofer_exp)
tweeter_volt = sy.lambdify([f, C], tweeter_exp)

#print(woofer_exp)
