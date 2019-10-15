import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from matplotlib.animation import FuncAnimation

from dft import dft
from load_json import load_json


class Clock(object):
    def __init__(self, start_pos, radius, angle):

        self.radius = radius
        self.angle = angle
        self.start_pos = start_pos
        self.end_pos = self.start_pos + self.radius * np.array((np.cos(self.angle), np.sin(self.angle)))

        self.draw()


    def get_circle_patch(self):
        self.circ_patch = Circle(self.start_pos, self.radius, fill=False)
        return self.circ_patch

    def get_line(self):
        xdata = (self.start_pos[0], self.end_pos[0])
        ydata = (self.start_pos[1], self.end_pos[1])
        self.line = Line2D(xdata, ydata, linewidth=0.5)
        return self.line

    def draw(self):
        plt.gca().add_patch(self.get_circle_patch())
        plt.gca().add_line(self.get_line())
        

def func(frame, ax1, clocks):
    artists = []

    for clock in clocks:
        clock.draw()
    
    return artists

def init():
    plt.gca().set_xlim(-50, 50)
    plt.gca().set_ylim(-50, 50)
    plt.gca().set_aspect(1)
    return []

def main():
    fig1, ax1 = plt.subplots()

    N = 3
    clocks = []

    position = np.array((0,0))
    radius = 0.2
    angle = 0
    for i in range(N):
        clocks.append(Clock(position, radius, angle))
        position = clocks[-1].end_pos
        radius += 0.2
        angle += np.deg2rad(30)

    anim = FuncAnimation(fig1, func, frames=None, init_func=init, fargs = (ax1, clocks), interval=100, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    main()
