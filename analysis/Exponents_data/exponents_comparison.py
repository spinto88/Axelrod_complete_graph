import pandas as pd 
import matplotlib.pyplot as plt
    
exponents_er = pd.read_csv('Exponents_ER.dat', index_col = 0, header = None)

pc, nu, beta, gamma = [],[],[],[]
Fs = [10, 25, 50, 100]#, 250]

for F in Fs:

    exponents = pd.read_csv('Exponents_F{}.dat'.format(F), index_col = 0, header = None)

    pc.append(exponents.loc['pc'].tolist()) 
    nu.append(exponents.loc['nu'].tolist()) 
    beta.append(exponents.loc['beta'].tolist()) 
    gamma.append(exponents.loc['gamma'].tolist()) 

fig = plt.figure(1, figsize = (5,3))
ax = plt.axes([0.225, 0.20, 0.675, 0.70])

ax.errorbar(Fs, [x[0] for x in pc], [x[1] for x in pc], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['pc'].tolist()
ax.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15, label = 'ER')
ax.plot(range(0,250), [er]*250, '--', linewidth = 2, color = 'k', alpha = 0.50)
ax.grid(alpha = 0.15)
ax.set_xlabel(r'$F$', size = 20)
ax.set_ylabel(r'$p_{int}^c(\infty)$', size = 20)
ax.set_xscale('symlog')
ax.set_xticks(Fs)
ax.set_xticklabels(Fs, size = 12)
ax.set_xlim([5, 150])
ax.xaxis.set_label_coords(1.05, 0.00)
plt.legend(loc = 'best', fontsize = 12)
plt.savefig('Pc_comparison.png', dpi = 600)

fig = plt.figure(2, figsize = (5,3))
ax = plt.axes([0.225, 0.20, 0.675, 0.70])

ax.errorbar(Fs, [x[0] for x in nu], [x[1] for x in nu], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['nu'].tolist()
ax.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15, label = 'ER')
ax.plot(range(0,250), [er]*250, '--', linewidth = 2, color = 'k', alpha = 0.50)
ax.grid(alpha = 0.15)
ax.set_xscale('symlog')
ax.set_xticks(Fs)
ax.set_xticklabels(Fs, size = 12)
ax.set_xlim([5, 150])
ax.xaxis.set_label_coords(1.05, 0.00)
ax.set_xlabel(r'$F$', size = 20)
ax.set_ylabel(r'$\nu$', size = 20)
ax.legend(loc = 'best', fontsize = 12)
plt.savefig('Nu_comparison.png', dpi = 600)

fig = plt.figure(3, figsize = (5,3))
ax = plt.axes([0.225, 0.20, 0.675, 0.70])
ax.errorbar(Fs, [-x[0] for x in beta], [x[1] for x in beta], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['beta'].tolist()
ax.fill_between(range(0,250), [-er - er_error]*250,  [-er + er_error]*250, color = 'k', alpha = 0.15, label = 'ER')
ax.plot(range(0,250), [-er]*250, '--', linewidth = 2, color = 'k', alpha = 0.50)
ax.grid(alpha = 0.15)
ax.set_xscale('symlog')
ax.set_xticks(Fs)
ax.set_xticklabels(Fs, size = 12)
ax.set_xlim([5, 150])
ax.xaxis.set_label_coords(1.05, 0.00)
ax.set_xlabel(r'$F$', size = 20)
ax.set_ylabel(r'$\beta / \nu$', size = 20)
ax.legend(loc = 'best', fontsize = 12)
plt.savefig('Beta_comparison.png', dpi = 600)


fig = plt.figure(4, figsize = (5,3))
ax = plt.axes([0.225, 0.20, 0.675, 0.70])
ax.errorbar(Fs, [x[0] for x in gamma], [x[1] for x in gamma], fmt = '.', markersize = 15, alpha = 0.75, color = 'red')
er, er_error = exponents_er.loc['gamma'].tolist()
ax.fill_between(range(0,250), [er - er_error]*250,  [er + er_error]*250, color = 'k', alpha = 0.15, label = 'ER')
ax.plot(range(0,250), [er]*250, '--', linewidth = 2, color = 'k', alpha = 0.50)
ax.grid(alpha = 0.15)
ax.set_xscale('symlog')
ax.set_xticks(Fs)
ax.set_xticklabels(Fs, size = 12)
ax.set_xlim([5, 150])
ax.xaxis.set_label_coords(1.05, 0.00)
ax.set_xlabel(r'$F$', size = 20)
ax.set_ylabel(r'$\gamma / \nu$', size = 20)
ax.legend(loc = 'best', fontsize = 12)
plt.savefig('Gamma_comparison.png', dpi = 600)

plt.show()
