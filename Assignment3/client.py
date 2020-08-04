import json
import requests
import numpy as np

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11


#### functions that you can call
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -1<=abs(i)<=1
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -1<=abs(i)<=1
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

ini_arr = [-0.99916927573251173823,  0.9990953590656609808, -0.9997318695245183, 0.99922889556431192, 0.03587507175384199, -0.0015634754169704097, -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]

if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """
    # arr = input('Enter Coefficients: ')
    # print(arr)
    validation_err = 10**14
    train_err = 10**14
    first = ini_arr[4]
    for i in range(100):
    	# first = ini_arr[0]
    	# ini_arr[2] = first - i*10**-3 - round(first,3) + round(first,2)
    	ini_arr[4] = first + i*10**-2 - round(first,2)
    	print(ini_arr[4])
    	# quit()
    	err = get_errors('3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp', ini_arr)
    	assert len(err) == 2
    	print(err)
    	if(validation_err>err[0]):
    		validation_err = err[0]
    	if(train_err>err[1]):
    		train_err = err[1]
    print(validation_err,train_err)

    # submit_status = submit('3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp', list(-np.arange(0,1.1,0.1)))
    # assert "submitted" in submit_status
    
