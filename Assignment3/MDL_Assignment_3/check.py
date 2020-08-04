arr = [0.0, 0.180804647374809, -6.6839923876448974, 0.06601482061378425, 0.03844843039136505, 8.898715387530427e-05, -5.999388040307434e-05, -1.2337528602820766e-07, 3.455586485848311e-08, 3.6319361801218085e-11, -6.627664932258919e-12]
arr = [[0.0, 0.1264795618911298, -6.446467789609297, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12612822760368578, -6.446467789609297, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12559801743342064, -6.430027156230421, 0.05420188252151272, 0.03844843039136505, 8.415792510364831e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.1264795618911298, -6.421262293009345, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12612822760368578, -6.471445987842753, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12559801743342064, -6.446467789609297, 0.05416873076673235, 0.03844843039136505, 8.467215462168631e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12616035228732908, -6.430027156230421, 0.053705927708615354, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12559801743342064, -6.484079666699487, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.867289907666504e-11, -6.6387499060899005e-12],
[0.0, 0.12559801743342064, -6.430027156230421, 0.05420188252151272, 0.03849586814933248, 8.415792510364831e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.1264795618911298, -6.446467789609297, 0.05416873076673235, 0.03844843039136505, 8.415792510364831e-05, -5.999388040307434e-05, -1.2486424474018939e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.1264795618911298, -6.484079666699487, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.60158921921083e-12],
[0.0, 0.1264795618911298, -6.446467789609297, 0.05416873076673235, 0.03844843039136505, 8.446046784391922e-05, -5.999388040307434e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.586592639835782e-12],
[0.0, 0.12616035228732908, -6.430027156230421, 0.053705927708615354, 0.03844843039136505, 8.477365840582838e-05, -5.971974601584964e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12],
[0.0, 0.12616035228732908, -6.430027156230421, 0.0547567719409559, 0.03844843039136505, 8.410997007267534e-05, -6.0477936308488645e-05, -1.243960488864828e-07, 3.455586485848311e-08, 3.87533631638698e-11, -6.638115645437453e-12],
[0.0, 0.12559801743342064, -6.430027156230421, 0.05420188252151272, 0.03844843039136505, 8.415792510364831e-05, -6.050203748447249e-05, -1.2415653359793733e-07, 3.455586485848311e-08, 3.8953734489501946e-11, -6.6387499060899005e-12]]

API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11
import random
import json
import requests
import numpy as np
import time
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
for i in arr:
    err = get_errors('UNmhf3Kv18sOotABqtxAA5wNtrF7ov2Hl4mRkWjgM0o2OfEw71', i)
    assert len(err) == 2
    print(i)
    print(err)
    print(err[0]+err[1])