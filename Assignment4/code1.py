import numpy as np
import math
num_of_features = 3
f=[
	        [1.5,450,220,'N'],
            [4.5,520,-120,'N'],
            [3,490,120,'Y'],
            [5.5,530,117,'Y'],
            [3.2,470,-170,'N'],
            [5.2,505,-90,'Y'],
            [1.85,465,120,'Y'],
            [4.8,517,147,'Y'],
            [1.7,430,-100,'Y']
	]
f2=[
	        [1.5,450,220,'N'],
            [4.5,520,-120,'N'],
            [3,490,120,'Y'],
            [5.5,530,117,'Y'],
            [3.2,470,-170,'N'],
            [5.2,505,-90,'Y'],
            [1.85,465,120,'Y'],
            [4.8,517,147,'Y'],
            [1.7,430,-100,'Y']
	]

def level(ff,idx):
	gain = 0
	selected_feature = 0
	num_of_features = len(ff[0])-1
	entropy_of_set = calc_entropy(ff)
	# print(entropy_of_set)
	keys = calc_unique(ff,idx)
	r = 0 
	# print(keys)
	for i in keys:
		p=0
		n=0
		for row in ff:
			if i==row[idx] and row[num_of_features]=='Y':
				p+=1
			elif i==row[idx]  and row[num_of_features]=='N':
				n+=1
		# print(p,n)
		r += ((n+p)/(len(f)))*calc_B(p/(p+n))
		
	g = entropy_of_set-r
	return r 
	# return g

def split_data(ff,p,idx):
	# print(ff)
	for i in range(len(ff)):
		if(ff[i][idx]<=p):
			ff[i][idx] = 'a'
		else:
			ff[i][idx] = 'b'
	return ff

def calc_entropy(a):
	l = len(a[0])
	b = []
	for i in a:
		b.append(i[l-1])
	# print(b)
	keys, values = np.unique(b,return_counts=True)
	sum_v = values.sum()
	res = list(map(lambda a: -(a/sum_v)*math.log2(a/sum_v), values))
	sum_v = sum(res)
	# print(sum_v)
	return sum_v

def calc_unique(a,idx):
	keys = []
	for i in a:
		if i[idx] not in keys:
			keys.append(i[idx])
	return keys

def calc_B(q):
	if q==0:
		return -(1-q)*(math.log2(1-q))
	elif q==1:
		return -q*math.log2(q) 
	return -(q*math.log2(q)+(1-q)*(math.log2(1-q)))
for i in range(3):
	g = []
	# qwe = f
	for j in f:
		split_point = j[i]
		data  = split_data(f,split_point,i)
		# print(f)
		# print(data)
		g.append(level(data,i))
		for k in range(len(f2)):
			f[k][i] = f2[k][i]
		
	print(g)
	print('==================================================================')


# arr = [f]
# while len(arr):
# 	brr = []
# 	for ar in arr:
# 		print("New branch")
# 		idx = level(ar)
# 		keys = calc_unique(ar,idx)
# 		for val in keys:
# 			a = []
# 			uq = []
# 			for f in ar:
# 				if(f[idx]==val):
# 					a.append(f[0:idx]+f[idx+1:])
# 					if f[-1] not in uq:
# 						uq.append(f[-1])
# 			if(len(uq)==1):
# 				print("LEAF")
# 			else:
# 				brr.append(a)
# 	arr = brr