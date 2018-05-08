#!/usr/bin/python

import sys
import pandas as pd
import numpy as np
import random

def gen_matSPD(dim):
	dim = int(dim)
	mat = pd.DataFrame()

	for i in range(dim):
		list=[random.randrange(-100, 100) for j in range(i)]
		for n in range(dim-1-i):
			list.append(0)
		list = pd.DataFrame(list)
		mat=pd.concat([mat,list], axis=1)

	mat = np.dot(mat, np.transpose(mat))

	with open('matrizSPD.txt','wb') as f:
	    for line in mat:
	        np.savetxt(f, line, fmt='%.2f')
	f.close()

if __name__ == "__main__":
	gen_matSPD(sys.argv[1])
