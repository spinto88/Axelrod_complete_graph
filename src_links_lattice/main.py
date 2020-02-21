from axelrod_py import *
import ast
import os

N = 100
F = 10

np.random.seed(123454)

p2q = lambda x, f: int((1.00 - ((1.00 - x)**(1./f)))**(-1))

for p in [0.05, 0.10, 0.15, 0.20, 0.25, 0.50, 0.90]:

  for F in [5, 10, 100]:

    q = p2q(p, F)
    for i in range(10):

        mysys = Axl_network(n = N, f = F, q = q, topology = 'lattice')
        mysys.evol2convergence()

	fp = open("Links_created_destroyed", "r").readlines()
	data = [[ast.literal_eval(j) for j in i.split(',')] for i in fp]

	fp = open('Links_F{}_N{}_p{}.dat'.format(F,N,p),'a')
	fp.write("{},{}\n".format(np.sum([d[0] for d in data]), np.sum([d[1] for d in data])))
	fp.close()

	os.remove("Links_created_destroyed")

