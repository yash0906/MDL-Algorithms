import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
from operator import add,sub
infile = open('data.pkl', 'rb') # loading the data and storing in obj
obj = pickle.load(infile)
infile.close()
X = obj[:,0:1]
Y = obj[:,1:2]
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.1, random_state=1) #splitting the data into training and testing
# for each poly,we need to train a model on 10 datasets 
train_size = len(X_train)
test_size = len(y_test)
data_size = int(train_size/10) #size of smaller training model
avg_bias = []#size of this will be number of possible degree of ploynomials
avg_var = []# size of this will be number of possible degree of ploynomials
# print(X_test.shape)
# deg = int(input("Enter No. of Degree: "))
deg = 10
for i in range(1,deg):#this is the degree of the ploynomial
	expected = np.zeros(test_size) # expected value of the predicted data
	comp_y_pred = [] # this contain predicted value of all the training model
	for j in range(0,train_size,data_size):
		poly = PolynomialFeatures(degree=i)
		X_poly_train = poly.fit_transform(X_train[j:j+data_size,0:1])
		X_poly_test = poly.fit_transform(X_test)
		regressor = LinearRegression()
		regressor.fit(X_poly_train,y_train[j:j+data_size,0:1])
		y_pred = regressor.predict(X_poly_test)
		comp_y_pred.extend(y_pred[:,0:1])
		expected = list(map(add, expected, y_pred[:,0:1]))
	
	expected = np.array(expected)/10
	
	varience = np.zeros(test_size)
	for k in range(test_size):
		for l in range(10):
			varience[k] += (comp_y_pred[test_size*l+k]-expected[k])**2
		# varience[k]*=100

	varience = np.array(varience)/10
	avg_var.append(np.mean(varience))

	bias = list(map(sub, expected, y_test))

	bias = np.square(bias)
	avg_bias.append(np.mean(bias))
xx = np.arange(1,deg)
print("Bias square:	")
for i in avg_bias:
	print(i)
print("Varience:	")
for i in avg_var:
	print(i)
# print(avg_bias)
# print(avg_var)
# plt.plot(xx,avg_bias, marker='*', color='green')
# plt.plot(xx,avg_var, marker='*', color='red')

# plt.xlabel('x-axix')
# plt.ylabel('Bias')
plt.show()
# plt.savefig('bias.png')