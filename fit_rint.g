M=0.45 #initial parameter
Sigma=0.002 #sigma y. find a way to add to the fit

y(x)=M

#plot experimental data
plot "./data/internal_resistance.txt" using 1:2

fit y(x) "./data/internal_resistance.txt" u 1:2 via M

Rg=47.26*(1/M-1)

print Rg

