from axelrod_py import *

N = 100
F = 100

np.random.seed(123457)

k2q = lambda x, N, f: int(-f*(np.log(1.00 - float(x)/N)**(-1)))

for k in np.linspace(0.10, 5.00, 81):

  q = k2q(k, N, F)

  mysys = Axl_network(n = N, f = F, q = q)

  mysys.evol2convergence()

  mysys.save_fragments_distribution('N{}_F{}.dat'.format(N, F))


