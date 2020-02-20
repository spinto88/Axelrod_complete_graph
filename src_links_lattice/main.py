from axelrod_py import *
import ast
import os

N = 225
F = 10

np.random.seed(123454)

k2q = lambda x, f: int((1.00 - (1.00 - x)**(1./f))**(-1))

p = 0.20

for F in [5, 10, 25, 50, 100]:

    q = k2q(p, F)
    for i in range(25):
        mysys = Axl_network(n = N, f = F, q = q, topology = 'lattice')
        mysys.evol2convergence()

	fp = open("Links_created_destroyed", "r").readlines()
	data = [[ast.literal_eval(j) for j in i.split(',')] for i in fp]

	fp = open('Links_F{}_N{}.dat'.format(F,N),'a')
	fp.write("{},{}\n".format(np.sum([d[0] for d in data]), np.sum([d[1] for d in data])))
	fp.close()

	os.remove("Links_created_destroyed")

