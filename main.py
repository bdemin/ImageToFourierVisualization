import numpy as np
import sys

import pygame

from dft import dft
from load_json import load_json


class Graphics(object):
    def __init__(self):

        pygame.init()
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size, 0, 32)
        self.clock = pygame.time.Clock()
     

    def init_callback(self, epicycles):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill((0, 0, 0))
            time = pygame.time.get_ticks()/1000

            flag = True
            for epicycle in epicycles:
                if flag:
                    epicycle.update((400, 300), time)
                    last_center_pos = epicycle.dial_end_pos
                    flag = False
                else:
                    epicycle.update(last_center_pos, time)
                    last_center_pos = epicycle.dial_end_pos
                epicycle.move()

            pygame.display.flip()
            self.clock.tick(100)


class Epicycle(object):
    def __init__(self, screen, amp, freq, phase, center_pos):
        # Create Epicycle object to store signal data for visualization

        self.screen = screen
        
        self.amp = amp
        self.freq = freq
        self.phase = phase
        self.center_pos = center_pos
        
        self.update(self.center_pos, 0)



    def update(self, center_pos, time):
        # Update center and end positions in time
        
        self.center_pos = center_pos
        phi = self.freq * time + self.phase
        self.dial_end_pos = self.center_pos + self.amp * np.array((np.cos(phi), np.sin(phi)))
        self.dial_end_pos = (int(self.dial_end_pos[0]), int(self.dial_end_pos[1]))
    
    def move(self):
        # self.circle.move(self.center_pos)
        self.circle = pygame.draw.circle(self.screen, (255, 255, 255),
                                        self.center_pos, self.amp, 1)
        self.line = pygame.draw.line(self.screen, (255, 255, 255),
                                        self.center_pos, self.dial_end_pos, 2)



def build_data(N):
    
    center_pos = (400, 300)
    amp = 100
    freq = -1
    phase = 0

    data = []
    for i in range(N):
        data.append({'amp': amp, 'freq': freq, 'phase': phase})
        amp = int(amp * 0.6)
        freq *= 1.5
        phase -= np.pi/4
    return data

def build_epicycles(N, screen, data):
    
    epicycles = []
    center_pos = (0,0)
    for i in range(N):
        epicycles.append(Epicycle(screen, data[i]['amp'], data[i]['freq'], data[i]['phase'], center_pos))
        center_pos = epicycles[-1].dial_end_pos
    return epicycles


def main():
    NUM_CYC = 5

    graphics = Graphics()

    data = build_data(NUM_CYC)

    epicycles = build_epicycles(NUM_CYC, graphics.screen, data)

    graphics.init_callback(epicycles)


if __name__ == '__main__':
    main()
