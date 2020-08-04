import numpy as np 
import time
import os
states = []
Ut = {}
Ut1 = {}
#team number 89
current_dir = os.getcwd()
final_dir = os.path.join(current_dir, 'outputs')
os.makedirs(final_dir)
for i in range(5):
	for j in range(4):
		for k in range(3):
			states.append((i,j,k))#(health,arrow,stamina)
			Ut[(i,j,k)]=0
			Ut1[(i,j,k)]=0

itr=0
k=0
for i in range(4):
	if(i==0):
		f=open('outputs/task_1_trace.txt','w')
		step_cost=-5
		shoot_step_cost = -5
		df=0.99
		delta = 0.001
	elif(i==1):
		f=open('outputs/task_2_part_1_trace.txt','w')
		step_cost=-2.5
		shoot_step_cost = -0.25
		df=0.99
		delta = 0.001
	elif(i==2):
		f=open('outputs/task_2_part_2_trace.txt','w')
		step_cost=-2.5
		shoot_step_cost = -2.5
		df=0.1
		delta = 0.001
	else:
		f=open('outputs/task_2_part_3_trace.txt','w')
		step_cost=-2.5
		shoot_step_cost = -2.5
		df=0.1
		delta=0.0000000001
	for key in Ut:
		Ut[key]=0
		Ut1[key]=0

	itr=0
	k=0
	while True:
		# print("iteration="+str(itr))
		f.write("iteration="+str(itr) + '\n')
		itr+=1
		for j in states:
			if(j[0]==0):
				Ut1[j]=0
				k+=1
				# print(str(j)+':-1=[0.]')
				f.write('(' + str(j[0]) + ',' + str(j[1]) + ',' + str(j[2])+')'+':-1=[0.]' + '\n')
				continue
			#shoot
			shoot=-1000000
			if(j[1]>0 and j[2]>0):
				shoot = shoot_step_cost + df*(0.5*Ut[(j[0],j[1]-1,j[2]-1)] + 0.5*Ut[(j[0]-1,j[1]-1,j[2]-1)])
				if(j[0]==1):
					shoot+=5

			#recharge
			recharge = -1000000
			if(j[2]==2):
				recharge = step_cost+ df*Ut[j]
			else:
				recharge = step_cost + df*(0.8*Ut[(j[0],j[1],j[2]+1)] + 0.2*Ut[j])

			#dodge
			dodge = -1000000
			if(j[2]>0):
				if(j[2]==2):
					dodge = step_cost + df*(0.8*0.8*Ut[(j[0],min(3,j[1]+1),1)] + 0.8*0.2*Ut[(j[0],j[1],1)] + 0.2*0.8*Ut[(j[0],min(3,j[1]+1),0)] + 0.2*0.2*Ut[(j[0],j[1],0)])
				else:
					dodge = step_cost + df*(0.8*Ut[(j[0],min(3,j[1]+1),0)] + 0.2*Ut[(j[0],j[1],0)])

			mak = max(shoot,recharge,dodge)
			Ut1[j]=mak
			# print(Ut[j],Ut1[j])
			if(abs(Ut[j]-Ut1[j])<delta):
				k+=1

			if(mak==shoot):
				# print('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):SHOOT=[" + str('{0:.8f}'.format(mak)) + ']')
				f.write('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):SHOOT=[" + str('{0:.3f}'.format(mak)) + ']' + '\n')
			elif(mak==recharge):
				# print('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):RECHARGE=[" + str('{0:.8f}'.format(mak)) + ']')
				f.write('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):RECHARGE=[" + str('{0:.3f}'.format(mak)) + ']' + '\n')
			else:
				# print('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):DODGE=[" + str('{0:.8f}'.format(mak)) + ']')
				f.write('(' + str(j[0]) + ',' + str(j[1])+','+str(j[2])+"):DODGE=[" + str('{0:.3f}'.format(mak)) + ']' + '\n')
		for key in Ut:
			Ut[key] = Ut1[key]
		# time.sleep(1)
		# print()
		# print()
		f.write('\n')
		f.write('\n')
		if(k==60):
			break
		k=0
