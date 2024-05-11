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
R, V, w, f, L, C,k = sy.symbols("R V w f L C k")

# Define voltage functions

#with pulsation
# Tweeter
woofer_exp = R*V/sy.sqrt(R**2+(w*L)**2)
#Woofer
tweeter_exp = R*V/sy.sqrt(R**2+(w*C)**-2)

#Phase functions
woofer_phase_exp = sy.atan(-w*L/R)
tweeter_phase_exp = sy.atan(1/(w*R*C))


#Conversion
# Frequency to angular frequency
f_conv = 2*sy.pi*f

#Switch to frequency and add parameters
tweeter_exp=tweeter_exp.subs(R,c.Res1).subs(V,c.Vin).subs(w,f_conv)
woofer_exp=woofer_exp.subs(R,c.Res2).subs(V,c.Vin).subs(w,f_conv)

tweeter_phase_exp = tweeter_phase_exp.subs(R,c.Res1).subs(w,f_conv)
woofer_phase_exp = woofer_phase_exp.subs(R,c.Res2).subs(w,f_conv)

#Commodity functions
phase_sum_exp=tweeter_phase_exp+woofer_phase_exp
#phase_diff_exp=sy.abs(tweeter_phase_exp-woofer_phase_exp)
p_diff=tweeter_phase_exp-woofer_phase_exp+k


#Create lambdas
woofer_volt = sy.lambdify([f, L], woofer_exp)
tweeter_volt = sy.lambdify([f, C], tweeter_exp)

tweeter_phase = sy.lambdify([f, C], tweeter_phase_exp)
woofer_phase = sy.lambdify([f, L], woofer_phase_exp)
phase_difference=sy.lambdify([f, L, C, k], p_diff)

#print(woofer_exp)
