import pandas as pd 
import matplotlib.pyplot as plt
    
exponents_er = pd.read_csv('Exponents_ER.dat', index_col = 0, header = None)

pc, nu, beta, gamma = [],[],[],[]
Fs = [10, 20, 100]

for F in Fs:

    exponents = pd.read_csv('Exponents_F{}.dat'.format(F), index_col = 0, header = None)

    pc.append(exponents.loc['pc'].tolist()) 
    nu.append(exponents.loc['nu'].tolist()) 
    beta.append(exponents.loc['beta'].tolist()) 
    gamma.append(exponents.loc['gamma'].tolist()) 

plt.figure(1, figsize = (5,3))
plt.axes([0.24, 0.25, 0.70, 0.65])
plt.errorbar(Fs, [x[0] for x in pc], [x[1] for x in pc], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['pc'].tolist()
plt.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15)
plt.grid(alpha = 0.15)
plt.xlabel(r'$F$', size = 15)
plt.ylabel(r'$p_c(\infty)$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.savefig('Pc_comparison.png', dpi = 600)

plt.figure(2, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.errorbar(Fs, [x[0] for x in nu], [x[1] for x in nu], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['nu'].tolist()
plt.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15)
plt.grid(alpha = 0.15)
plt.xlabel(r'$F$', size = 15)
plt.ylabel(r'$\nu$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.savefig('Nu_comparison.png', dpi = 600)

plt.figure(3, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.errorbar(Fs, [-x[0] for x in beta], [x[1] for x in beta], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['beta'].tolist()
plt.fill_between(range(0,250), [-er - er_error]*250,  [-er + er_error]*250, color = 'k', alpha = 0.15)
plt.grid(alpha = 0.15)
plt.xlabel(r'$F$', size = 15)
plt.ylabel(r'$\beta$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.savefig('Beta_comparison.png', dpi = 600)

plt.figure(4, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.errorbar(Fs, [x[0] for x in gamma], [x[1] for x in gamma], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['gamma'].tolist()
plt.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15)
plt.grid(alpha = 0.15)
plt.xlabel(r'$F$', size = 15)
plt.ylabel(r'$\gamma$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.savefig('Gamma_comparison.png', dpi = 600)

plt.show()
