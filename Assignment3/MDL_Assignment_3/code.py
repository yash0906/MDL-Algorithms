import random
import json
import requests
import numpy as np 
import csv
gbl = []
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

#### functions that you can call
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

#### utility functions
def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


class Individual(object):

	def __init__(self,chromo):
		self.chromo = chromo#chromosome
		self.err = self.calc_error() #error array
		self.fitness = self.err[0] + self.err[1] #fittness value
		self.fit_diff = abs(self.err[0] - self.err[1]) # difference of error
		self.fit_sum = self.err[0] + self.err[1] #sum of error

	def calc_error(self):
		err = get_errors('3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp', self.chromo)
		assert len(err) == 2
		return err

	def mate(self,param):
		# 2 point cross over
		# ----------------------------------------------------------------------
		child_chromo = []
		# k = random.randint(1,5)
		# for i in range(0,k):
		# 	child_chromo.append(self.chromo[i])
		# p = random.randint(k+1,10)
		# for i in range(k,p):
		# 	child_chromo.append(param.chromo[i])
		# for i in range(p,11):
		# 	child_chromo.append(self.chromo[i])
		
		# random crossover
		#------------------------------------------------------------------------- 
		for i in range(11):
			prob = random.uniform(0,1)
			if prob<0.5:
				child_chromo.append(self.chromo[i])
			else:
				child_chromo.append(param.chromo[i])
		
		# mutation
		# ----------------------------------------------------------------------
		for i in range(11):
			prob = random.uniform(0,1)
			if prob<0.2:
				g  = child_chromo[i]
				if g>0:
					child_chromo[i] = (random.uniform(g-g/20,min(10,g+g/20)))
				else:
					child_chromo[i] = (random.uniform(max(-10,g/20+g),g-g/20))  
		# --------------------------------------------------------------------
		return Individual(child_chromo)
		# this is one of the crossover and mutation we tried
		# for g1,g2 in zip(self.chromo,param.chromo):
		# 	prob = random.random()

		# 	if prob < 0.42:
		# 		child_chromo.append(g1)
		# 	elif prob < .85:
		# 		child_chromo.append(g2)
		# 	else:
		# 		prob = random.random()
		# 		if prob<0.5:
		# 			if g1>0:
		# 				child_chromo.append(random.uniform(g1-g1/10,min(10,g1+g1/10)))
		# 			else:
		# 				child_chromo.append(random.uniform(max(-10,g1/10+g1),g1-g1/10))
		# 		else:
		# 			if g2>0:
		# 				child_chromo.append(random.uniform(g2-g2/10,min(10,g2+g2/10)))
		# 			else:
		# 				child_chromo.append(random.uniform(max(-10,g2/10+g2),g2-g2/10))
		# return Individual(child_chromo)


overfit = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
population = []
# generating initial population
# -------------------------------------------------------------------
for i in range(10):
	arr1  = [random.uniform(g-g/2,min(10,g+g/2)) if g>0 else random.uniform(max(-10,g+g/2),g-g/2) for g in overfit]
	population.append(Individual(arr1))

# if you want to want take your best population, place them in a arr list here
# for i in arr:
	# population.append(Individual(i))

population_size = len(population)

print('Population',population_size)

generation = 1
while True:
	print("Generation: ",generation)
	generation+=1
	# sorting population on the basis of fitness
	population = sorted(population, key = lambda x:(x.fitness))
	for i in population:	
		print(i.chromo)
		print("\033[92m" + str(i.fitness) + "\033[00m")
		print("\033[93m" + str(i.fit_sum) + "\033[00m")
		print("\033[91m" + str(i.fit_diff) + "\033[00m")
	new_generation = []
	# top 10% population is directly passed into the next generation with mutation
	s = int((10*population_size)/100)
	new_generation.extend(population[:s])

	s = int((90*population_size)/100)
	for _ in range(s):
		parent1 = random.choice(population[:int(population_size/2)])#random parent from top 50% population 
		parent2 = random.choice(population[:int(population_size/2)])#random parent from top 50% population 
		# generating child through mating
		child = parent1.mate(parent2) 
		new_generation.append(child) 

	population = new_generation 
