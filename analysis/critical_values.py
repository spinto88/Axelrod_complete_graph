def read_data(fName):

    fp = open(fName,'r').read().split('\n')
    fp = [f.split(',') for f in fp[:len(fp)-1]]

    q = [int(f[1]) for f in fp]
    fragments = [[int(g) for g in f[2:]] for f in fp]

    return q, fragments

def biggest_fragment(fName):

    import numpy as np
    p, fragments = read_data(fName)

    p_range = sorted(list(set(p)))
    bigfrag_p = []

    for p_iter in p_range:
        frag_p = []
        for d in range(len(fragments)):
            if p[d] == p_iter:
                frag_p += [np.max(fragments[d])]

        bigfrag_p.append([p_iter, np.mean(frag_p)])

    return bigfrag_p

def average_fragment(fName):

    import numpy as np

    p, fragments = read_data(fName)

    p_range = sorted(list(set(p)))

    def mean_frag_function(frags):

        if len(frags) >= 1:
	    ms = np.sum(np.array(frags, dtype = np.float)**2)/np.sum(frags)
            return ms
        else:
            return 0.00

    bigfrag_p = []

    for p_iter in p_range:
        frag_p = []
        for d in range(len(fragments)):
            if p[d] == p_iter:
                aux = fragments[d]
                aux.remove(np.max(aux))
                frag_p += [mean_frag_function(aux)]

        bigfrag_p.append([p_iter, np.mean(frag_p)])

    return bigfrag_p

### Critical Data
import numpy as np
import pandas as pd

for F in [10, 25, 50, 100, 250, 1000]:

  data2save = []

  for N in [512, 768, 1024, 2048, 4096]:

    try:
      data_bigfrag = biggest_fragment('Data_nueva/Degree{}_F{}.dat'.format(N,F))
      data_fragments = average_fragment('Data_nueva/Degree{}_F{}.dat'.format(N,F))
   
      p = [b[0] for b in data_fragments]

      big_frag = [b[1]/N for b in data_bigfrag]
      average_s = [b[1] for b in data_fragments]

      critical_index = sorted(range(len(p)), reverse = True, key = lambda x: average_s[x])[0]
      critical_indexes = sorted(range(len(p)), reverse = True, key = lambda x: average_s[x])[:3]

      p_critical = np.average([p[i] for i in critical_indexes], weights = [average_s[i] for i in critical_indexes])
      big_frag_critical = np.average([big_frag[i] for i in critical_indexes], weights = [average_s[i] for i in critical_indexes])
      average_s_critical = np.average([average_s[i] for i in critical_indexes], weights = [average_s[i] for i in critical_indexes])

      data2save.append([N, p_critical, big_frag_critical, average_s_critical, critical_index])

    except:
      pass

  df = pd.DataFrame()
  df['N'] = [d[0] for d in data2save]
  df['Q'] = [d[1] for d in data2save]
  df['bigfrag'] = [d[2] for d in data2save]
  df['averagefrag'] = [d[3] for d in data2save]
  df['critical_index'] = [d[4] for d in data2save]
  df.to_csv('Data_processed/Critical_values_F{}.csv'.format(F), index = False)

