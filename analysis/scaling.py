import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

F = 1000

data = pd.read_csv('Data_processed/Critical_values_F{}.csv'.format(F))

### Non linear fitting

def non_linear_function(x, pc, b, nu):
    return  pc-b*(x**(-1.00/nu))

x = data['N']

q2p = lambda q,f: 1.00 - (1.00 - 1.00/q)**f

y = q2p(data['Q'], F)

popt, pcov = curve_fit(non_linear_function, x, y, bounds = ([0.00, -np.inf, 0.00], [1.00, np.inf, np.inf]))

print popt
perr = np.sqrt(np.diag(pcov))
print perr

fp = open('Exponents_data/Exponents_F{}.dat'.format(F),'w')
fp.write('pc,{},{}\n'.format(popt[0], perr[0]))
fp.write('nu,{},{}'.format(popt[2], perr[2]))
fp.write('\n')


plt.figure(1, figsize = (5,3))
plt.axes([0.15, 0.15, 0.75, 0.75])


plt.plot(x, y, '.', markersize = 20, alpha = 0.75, label = 'Data')
plt.plot(x, non_linear_function(x, *popt), '-', linewidth = 2, alpha = 0.50, label = 'Non-linear fit')

plt.xlabel('N', size = 20)
plt.ylabel(r'$p_{int}^c$', size = 20)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.grid(True, alpha = 0.15)
plt.legend(loc = 'best')
plt.savefig('images/pcN_F{}.png'.format(F), dpi = 300)
plt.show()

### Linear fit

plt.figure(1, figsize = (6,4))
plt.axes([0.20, 0.20, 0.70, 0.70])

pc = popt[0]

x = np.log2(data['N'])
y = np.log2(np.abs((q2p(data['Q'],F) - pc)))

coeffs, cov = np.polyfit(x, y, deg = 1, cov = True)
perr = np.sqrt(np.diag(cov))

fp.write('-1/nu,{},{}'.format(coeffs[0], perr[0]))
fp.write('\n')

plt.plot(x, y, '.', color = 'r', markersize = 25, alpha = 0.75)

plt.plot(x, x * coeffs[0] + coeffs[1], 'k-', linewidth = 2.5, alpha = 0.50) 

plt.grid(True, alpha = 0.25)
plt.xlabel(r'$log_2(N)$', size = 20)
plt.ylabel(r'$log_2(p_{int} - p_{int}^c)$', size = 20)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.grid(True, alpha = 0.15)
plt.savefig('images/pcN2_F{}.png'.format(F), dpi = 300)

plt.show()
exit()

### Linear fit Biggest Fragment

x = np.log2(data['N'])
y = np.log2(data['bigfrag'])

plt.figure(1, figsize = (6,4))
plt.axes([0.20, 0.20, 0.70, 0.70])

plt.plot(x, y, 'r.', markersize = 25, alpha = 0.75)
plt.grid(True, alpha = 0.25)
plt.xlabel(r'$log_2(N)$', size = 20)
plt.ylabel(r'$log_2(S_{max}/N)$', size = 20)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.grid(True, alpha = 0.15)
coeffs, cov = np.polyfit(x, y, deg = 1, cov = True)

beta = coeffs[0] 
beta_err = np.sqrt(np.diag(cov))[0]

fp.write('beta,{},{}'.format(beta, beta_err))
fp.write('\n')

plt.plot(x, x * coeffs[0] + coeffs[1], 'k-', linewidth = 2.5, alpha = 0.50) 
plt.savefig('images/PcN_F{}.png'.format(F), dpi = 300)



plt.show()


### Linear fit Average Fragment

plt.figure(1, figsize = (6,4))
plt.axes([0.20, 0.20, 0.70, 0.70])

x = np.log2(data['N'])
y = np.log2(data['averagefrag'])

plt.plot(x, y, 'r.', markersize = 25, alpha = 0.75)
plt.grid(True, alpha = 0.25)
plt.xlabel(r'$log_2(N)$', size = 20)
plt.ylabel(r'$log_2(\langle s \rangle)$', size = 20)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.grid(True, alpha = 0.15)
coeffs, cov = np.polyfit(x, y, deg = 1, cov = True)

gamma = coeffs[0] 
gamma_err = np.sqrt(np.diag(cov))[0]


fp.write('gamma,{},{}'.format(gamma, gamma_err))
fp.write('\n')
fp.close()

plt.plot(x, x * coeffs[0] + coeffs[1], 'k-', linewidth = 2.5, alpha = 0.50) 


plt.savefig('images/ScN_F{}.png'.format(F), dpi = 300)

plt.show()

