import numpy as np

from helpers import load_json, build_data, build_epicycles
from graphics import Graphics
from dft import dft


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
