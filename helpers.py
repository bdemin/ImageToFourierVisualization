import numpy as np
import json

from epicycle import Epicycle


def load_json(path):
    # Function to load a json file and convert it into np array
    
    with open(path) as f:
        data = json.loads(f.read())
        data = data['drawing']
        data = [[x['x'], x['y']] for x in data]

    skip = 10
    return np.asarray(data)[0 : -1 : skip]
    

def build_data(N):
    # Optional function to build and return signal data for all epicycles
    
    data = []

    # Arbitrary signal data
    amp = 100
    freq = -1
    phase = 0

    for i in range(N):
        data.append({'amp': amp, 'freq': freq, 'phase': phase})
        amp = int(amp * 0.6)
        freq *= 1.5
        phase -= np.pi/4
        
    return data


def build_epicycles(screen, data):
    # Function to build and return epicycle data
    # epicycles - list of dictionaries holding signal data
    
    epicycles = []
    center_pos = (0,0)

    for i in range(len(data)):
        epicycles.append(Epicycle(screen, data[i]['amp'], data[i]['freq'], data[i]['phase'], center_pos))
        center_pos = epicycles[-1].dial_end_pos

    return epicycles
