import math
import numpy

def ent_cal(data,val,f):
	cnt=0
	yes=0
	if(f==0):#greater or equal
		for i in range(9):
			if(data[i][0]>=val):
				cnt+=1
				if(data[i][3]=='Y'):
					yes+=1
	else:#less or equal
		for i in range(9):
			if(data[i][0]<=val):
				cnt+=1
				if(data[i][3]=='Y'):
					yes+=1
	print("yes=",end='')
	print(yes)
	print("cnt=",end='')
	print(cnt)
	
	if(cnt==0):
		py0=1
		pn0=1
	else:
		py0=yes/cnt
		pn0=1-py0
	
	if(yes==0):
		py0=1

	if(cnt==yes):
		pn0=1

	print("py0=",end='')
	print(py0)
	print("pn0=",end='')
	print(pn0)
	
	ent0=(py0*math.log2(py0)+pn0*math.log2(pn0))*(-1)
	

	print("ent0=",end='')
	print(ent0)
	
	cnt1=9-cnt
	yes1=6-yes
	if(cnt1==0):
		py1=1
		pn1=1
	else:
		py1=yes1/cnt1
		pn1=1-py1
	
	if(yes1==0):
		py1=1

	if(cnt1==yes1):
		pn1=1
	
	print()
	print()
	print("py1=",end='')
	print(py1)
	print("pn1=",end='')
	print(pn1)

	ent1=(py1*math.log2(py1)+pn1*math.log2(pn1))*(-1)
	
	print("ent1=",end='')
	print(ent1)
	x=cnt/10
	print("x=",end='')
	print(x)
	
	ent=(x)*ent0+(1-x)*ent1
	
	print()
	print("ent=",end='')
	print(ent)
	print("-----------------------------------------")
	print()
	
	return ent

if __name__ == "__main__":
	data=[
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
	v0=[]
	v1=[]
	g0=[]
	g1=[]
	for i in range(9):
		val=data[i][2]
		print(val)
		x=ent_cal(data,val,0)
		v0.append(x)
		g0.append(0.9182958340544896 - x)
		y=ent_cal(data,val,1)
		v1.append(y)
		g1.append(0.9182958340544896 - y)

	print(v0)
	print()
	print(g0)
	print()
	print(v1)
	print()
	print(g1)