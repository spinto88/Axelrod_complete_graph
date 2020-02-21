from axelrod_py import *
import ast
import os

N = 100
F = 10

np.random.seed(123454)

k2q = lambda x, N, f: int(-f*(np.log(1.00 - float(x)/N)**(-1)))

for k in [0.50, 1.00, 1.50, 2.00, 2.50]:

  for F in [5, 10, 25, 50, 100]:

    q = k2q(k, N, F)
    for i in range(10):

        mysys = Axl_network(n = N, f = F, q = q)
        mysys.evol2convergence()

	fp = open("Links_created_destroyed", "r").readlines()
	data = [[ast.literal_eval(j) for j in i.split(',')] for i in fp]

	fp = open('Links_F{}_N{}_k{}.dat'.format(F,N,k),'a')
	fp.write("{},{}\n".format(np.sum([d[0] for d in data]), np.sum([d[1] for d in data])))
	fp.close()

	os.remove("Links_created_destroyed")

