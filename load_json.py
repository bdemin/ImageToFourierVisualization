import json
import numpy as np


def load_json(path):
    # Function to load a json file and convert it into np array
    
    with open(path) as f:
        data = json.loads(f.read())
        data = data['drawing']
        data = [[x['x'], x['y']] for x in data]

    skip = 10
    return np.asarray(data)[0 : -1 : skip]
    