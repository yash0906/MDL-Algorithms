import cvxpy as cp
import numpy as np
import json
import os

S = {}# mapping states to their corresponding numbers
p=0
Q = {}# for each state storing their next states with probability for all 3 possible actions
for i in range(5):#health
	for j in range(4):#arrow
		for k in range(3):#stamina
			Q[(i,j,k)] = [{},{},{}]
			S[(i,j,k)]=p
			p+=1

actions = []
for j in S:
	# TERMINAL STATES
	if(j[0]==0):
		actions.append([j,0])
	# SHOOT
	if(j[1]>0 and j[2]>0 and j[0]>0):
		actions.append([j,1])
		Q[j][0][(j[0]-1,j[1]-1,j[2]-1)] = 0.500
		Q[j][0][(j[0],j[1]-1,j[2]-1)] = 0.500
		k+=1
	# DODGE
	if(j[2]>0 and j[0]>0):
		actions.append([j,2])
		if(j[2]==2):
			if(j[1]==3):
				Q[j][1][(j[0],j[1],j[2]-1)] = 0.800
				Q[j][1][(j[0],j[1],j[2]-2)] = 0.200
			else:		
				Q[j][1][(j[0],j[1],j[2]-1)] = 0.160
				Q[j][1][(j[0],j[1]+1,j[2]-1)] = 0.640
				Q[j][1][(j[0],j[1],j[2]-2)] = 0.040
				Q[j][1][(j[0],j[1]+1,j[2]-2)] = 0.160
		else:
			if(j[1]==3):
				Q[j][1][(j[0],j[1],j[2]-1)] = 1.000
			else:	
				Q[j][1][(j[0],j[1],j[2]-1)] = 0.200
				Q[j][1][(j[0],min(j[1]+1,3),j[2]-1)] = 0.800
		k+=1
	# RECHARGE
	if(j[2]!=2 and j[0]>0):
		actions.append([j,3])
		Q[j][2][(j[0],j[1],j[2]+1)] = 0.800
		Q[j][2][(j[0],j[1],j[2])] = 0.200
		k+=1
A = []
cols = len(actions)
A = [[0]*cols for i in range(60)]

for idx,ac in enumerate(actions):
	if(ac[1]==0):
		A[S[ac[0]]][idx]+=1
	else:
		for nxt,prob in Q[ac[0]][ac[1]-1].items():
			A[S[ac[0]]][idx]+=prob
			A[S[nxt]][idx]-=prob
A = np.reshape(A,(60,cols))
rewards = []
[rewards.append(0) if ac[1]==0 else rewards.append(-20) for ac in actions ]

rewards = np.reshape(rewards,(1,cols))
alpha = [0]*60
alpha[59]=1
alpha = np.reshape(alpha,(60,1))
X = cp.Variable((cols,1))
constraints = [(A @ X)==alpha,X>=0]
obj = cp.Maximize(rewards*X)
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:",prob.status)
print("Optimal value:",prob.value)
print("Optimal X:",X.value)
for j in S:
	S[j]=-10
X = np.reshape(X.value,(cols,))
for val,ac in zip(X,actions):
	if(S[ac[0]]<val):
		S[ac[0]] = val
		if(ac[1]==0):
			Q[ac[0]]='NOOP'
		elif(ac[1]==1):
			Q[ac[0]]='SHOOT'
		elif(ac[1]==2):
			Q[ac[0]]='DODGE'
		else:
			Q[ac[0]]='RECHARGE'
policy = []
[ policy.append([list(state),Q[state]]) for state in Q]
rewards = np.reshape(rewards,(100,))
alpha = np.reshape(alpha, (60,))
dict = {'a':A.tolist(),
		'r':rewards.tolist(),
		'alpha':alpha.tolist(),
		'x':X.tolist(),
		'policy':policy,
		'objective':float(prob.value),
		}
try:
	current_dir = os.getcwd()
	final_dir = os.path.join(current_dir, 'outputs')
	os.makedirs(final_dir)
except:
	pass
json_object = json.dumps((dict))
with open('outputs/output.json',"w") as f:
	f.write(json_object)
