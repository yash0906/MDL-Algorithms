import numpy as np
import math
num_of_features = 3
f = [['a','y','y','n'],
	['a','y','n','n'],
	['a','n','y','n'],
	['a','n','n','y'],
	['b','y','y','n'],
	['b','y','n','n'],
	['b','n','y','n'],
	['b','n','n','n'],
	['c','y','y','n'],
	['c','y','n','n'],
	['c','n','y','n'],
	['c','n','n','y']]
# f = [['s','h','h','w','n'],
# 	['s','h','h','s','y'],
# 	['o','h','h','w','y'],
# 	['r','m','h','w','y'],
# 	['r','c','n','w','y'],
# 	['r','c','n','s','y'],
# 	['o','c','n','s','y'],
# 	['s','m','h','w','n'],
# 	['s','c','n','w','y'],
# 	['r','m','n','w','y'],
# 	['s','m','n','s','y'],
# 	['o','m','h','s','y'],] 
# f = [['i','h','y','n'],
# 	['i','n','n','y'],
# 	['i','l','y','y'],
# 	['i','l','n','y'],
# 	['g','h','y','y'],
# 	['g','n','n','n'],
# 	['g','l','y','n'],
# 	['g','h','n','n'],
# 	['l','h','n','n'],
# 	['l','n','y','y'],
# 	['l','l','y','y'],
# 	['l','n','n','y'],]
# f = [['r','g','y','n'],
# 	['r','g','n','n'],
# 	['r','a','y','y'],
# 	['r','a','n','n'],
# 	['r','b','y','y'],
# 	['r','b','n','y'],
# 	['w','g','y','n'],
# 	['w','g','n','n'],
# 	['w','a','y','y'],
# 	['w','a','n','y'],
# 	['w','b','y','y'],
# 	['w','b','n','n'],] 
# f = [['c','s','y','y'],
# 	['c','s','n','n'],
# 	['c','o','y','y'],
# 	['t','s','n','n'],
# 	['t','s','y','y'],
# 	['t','o','y','y'],
# 	['i','s','y','y'],
# 	['i','s','n','n'],
# 	['i','o','n','y'],
# 	['u','o','y','y'],
# 	['u','s','n','n'],]  
def calc_entropy(a):
	l = len(a[0])
	b = []
	for i in a:
		b.append(i[l-1])
	print(b)
	keys, values = np.unique(b,return_counts=True)
	sum_v = values.sum()
	res = list(map(lambda a: -(a/sum_v)*math.log2(a/sum_v), values))
	sum_v = sum(res)
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
def level(f):
	gain = 0
	selected_feature = 0
	num_of_features = len(f[0])-1
	entropy_of_set = calc_entropy(f)
	print(entropy_of_set)
	for idx in range(num_of_features):
		keys = calc_unique(f,idx)
		r = 0 
		print(keys)
		for i in keys:
			p=0
			n=0
			for row in f:
				if i==row[idx] and row[num_of_features]=='y':
					p+=1
				elif i==row[idx]  and row[num_of_features]=='n':
					n+=1
			print(p,n)
			r += ((n+p)/(len(f)))*calc_B(p/(p+n))
		
		g = entropy_of_set-r
		print('entropy',r)
		print('gain',g)
		if(gain<g):
			gain = g
			selected_feature = idx
		# print('gain',gain)
	print(selected_feature,gain)
	return selected_feature
arr = [f]
while len(arr):
	brr = []
	print("NEW LEVEL")
	for ar in arr:
		print("NEW BRANCH")
		idx = level(ar)
		keys = calc_unique(ar,idx)
		for val in keys:
			a = []
			uq = []
			for f in ar:
				if(f[idx]==val):
					a.append(f[0:idx]+f[idx+1:])
					if f[-1] not in uq:
						uq.append(f[-1])
			if(len(uq)==1):
				print("THIS IS A LEAF")
			else:
				brr.append(a)
	arr = brr