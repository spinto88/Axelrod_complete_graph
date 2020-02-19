import pandas as pd 
import matplotlib.pyplot as plt
    
observables_er = pd.read_csv('Critical_values_ER.csv', header = 0)
Fs = [10, 20, 100]
color_dict = {10: 'r', 20: 'b', 100: 'm'}
q2p = lambda q,f: 1.00 - (1.00 - 1.00/q)**f

plt.figure(1, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.plot(observables_er['N'], observables_er['p'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    plt.plot(observables_f['N'], q2p(observables_f['Q'], F), '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))

plt.grid(alpha = 0.15)
plt.ylabel(r'$p_c(N)$', size = 15)
plt.xlabel(r'$N$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.legend(loc = 'best', fontsize = 10)

plt.figure(2, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.plot(observables_er['N'], observables_er['bigfrag'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    plt.plot(observables_f['N'], observables_f['bigfrag'], '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))

plt.grid(alpha = 0.15)
plt.ylabel(r'$S_{max}/N$', size = 15)
plt.xlabel(r'$N$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.legend(loc = 'best', fontsize = 10)

plt.figure(3, figsize = (5,3))
plt.axes([0.20, 0.25, 0.70, 0.65])
plt.plot(observables_er['N'], observables_er['averagefrag'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    plt.plot(observables_f['N'], observables_f['averagefrag'], '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))

plt.grid(alpha = 0.15)
plt.ylabel(r'$\langle s \rangle$', size = 15)
plt.xlabel(r'$N$', size = 15)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.legend(loc = 'best', fontsize = 10)

plt.show()
