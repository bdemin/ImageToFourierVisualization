import numpy as np

import pygame

from dft import dft
from load_json import load_json



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


def main():
    graphics = Graphics()

    graphics.drawing_mode()

    # NUM_CYCLES = 5
    # data = build_data(NUM_CYCLES)
    # file = 'train.json'
    # point_data = load_json(file)

    signal_data = dft(graphics.drawing_points)
    # signal_data = dft(point_data)

    graphics.epicycles = build_epicycles(graphics.screen, signal_data)

    graphics.init_callback()


if __name__ == '__main__':
    main()
