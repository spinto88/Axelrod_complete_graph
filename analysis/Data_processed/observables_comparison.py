import pandas as pd 
import matplotlib.pyplot as plt
    
observables_er = pd.read_csv('Critical_values_ER.csv', header = 0)
Fs = [10, 25, 50, 100]#, 250, 1000]
color_dict = {10: 'b', 25: 'g', 50: 'm', 100: 'r'}
q2p = lambda q,f: 1.00 - (1.00 - 1.00/q)**f

fig = plt.figure(1, figsize = (5,3))
ax = plt.axes([0.20, 0.20, 0.70, 0.70])
ax.plot(observables_er['N'], observables_er['p'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    ax.plot(observables_f['N'], q2p(observables_f['Q'], F), '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))

ax.set_ylabel(r'$p_{int}^c(N)$', size = 20)
ax.set_xlabel(r'$N$', size = 25)
ax.set_xscale('symlog')
ax.set_xticks([512, 768, 1024, 2048, 4096])
ax.set_xticklabels([512, 768, 1024, 2048, 4096], size = 12)
ax.minorticks_off()
ax.xaxis.set_label_coords(1.075, 0.00)
ax.legend(loc = 'best', fontsize = 10)
ax.grid(alpha = 0.15)
ax.set_xlim([450, 4500])
plt.savefig('pc_N.png', dpi = 600)

fig = plt.figure(2, figsize = (5,3))
ax = plt.axes([0.20, 0.20, 0.70, 0.70])
ax.plot(observables_er['N'], observables_er['bigfrag'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    ax.plot(observables_f['N'], observables_f['bigfrag'], '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))

ax.set_ylabel(r'$S_{max}^c/N$', size = 20)
ax.set_xlabel(r'$N$', size = 25)
ax.set_xscale('symlog')
ax.set_xticks([512, 768, 1024, 2048, 4096])
ax.set_xticklabels([512, 768, 1024, 2048, 4096], size = 12)
ax.minorticks_off()
ax.xaxis.set_label_coords(1.075, 0.00)
ax.grid(alpha = 0.15)
ax.set_xlim([450, 4500])
plt.savefig('Smaxc_N.png', dpi = 600)


fig = plt.figure(3, figsize = (5,3))
ax = plt.axes([0.20, 0.20, 0.70, 0.70])
ax.plot(observables_er['N'], observables_er['averagefrag'], '.-', markersize = 15, alpha = 0.75, color = 'k', label = 'ER')
for F in Fs:

    observables_f = pd.read_csv('Critical_values_F{}.csv'.format(F), header = 0)

    ax.plot(observables_f['N'], observables_f['averagefrag'], '.-', markersize = 15, alpha = 0.75, color = color_dict[F], label = 'F = {}'.format(F))


ax.set_ylabel(r'$\langle s \rangle^c$', size = 20)
ax.set_xlabel(r'$N$', size = 25)
ax.set_xscale('symlog')
ax.set_xticks([512, 768, 1024, 2048, 4096])
ax.set_xticklabels([512, 768, 1024, 2048, 4096], size = 12)
ax.set_yticklabels(range(2, 13, 2), size = 12)
ax.minorticks_off()
ax.xaxis.set_label_coords(1.075, 0.00)
ax.grid(alpha = 0.15)
ax.set_xlim([450, 4500])
plt.savefig('sc_N.png', dpi = 600)

plt.show()
