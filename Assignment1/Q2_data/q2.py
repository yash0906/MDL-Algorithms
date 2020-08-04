import pickle
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from operator import add,sub
file = open('Y_train.pkl','rb')
obj = pickle.load(file)
file.close()
y_train = obj
file = open('X_train.pkl', 'rb')
obj = pickle.load(file)
file.close()
X_train = obj
file = open('X_test.pkl', 'rb')
obj = pickle.load(file)
file.close()
X_test = obj  
file = open('Fx_test.pkl','rb')
obj = pickle.load(file)
file.close()
y_test = obj
# print(X_train.size,y_train.size, X_test.size, y_test.size)
test_size = y_test.size
data_size = 400
train_size = X_train.size
division = int(train_size/data_size)
# print(train_size)
avg_var = []
avg_bias = []
X_test = np.array(X_test)
X_test = X_test.reshape(-1,1)
# print(X_test.shape)
X_train = X_train.reshape(-1,1)
y_train = y_train.reshape(-1,1)
# deg = int(input("Enter No. of degree: "))
deg = 10
for i in range(1,deg):
	expected = np.zeros(test_size)
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
	
	expected = np.array(expected)/division
	
	varience = np.zeros(test_size)
	for k in range(test_size):
		for l in range(division):
			varience[k] += (comp_y_pred[test_size*l+k]-expected[k])**2

	varience = np.array(varience)/division
	avg_var.append(np.mean(varience))

	bias = list(map(sub, expected, y_test))
	
	bias = np.square(bias)
	avg_bias.append(np.mean(bias))
# quit()
# print(avg_bias)
xx = np.arange(1,deg)
ax = plt.subplot()
plt.plot(xx,avg_bias, marker='*', color='green' ,label='Bias^2')
plt.plot(xx,avg_var, marker='*', color='red' ,label='Varience')
ax.legend()
plt.xlabel('x-axix')
plt.ylabel('Bias^2/Varience')
plt.show()
# plt.savefig("bias-var.png")