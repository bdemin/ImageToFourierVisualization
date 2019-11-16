import numpy as np

import pygame

from dft import dft
from load_json import load_json


class Graphics(object):
    # Class to hold PyGame graphics data

    def __init__(self):
        pygame.init()
        self.screen_size = np.array((1200, 800))
        self.screen = pygame.display.set_mode(self.screen_size, 0, 32)
        self.clock = pygame.time.Clock()

        self.time = 0
        self.end_points = []

        self.is_drawing = True
        self.drawing_points = []
        self.last_point = (0,0)

    def drawing_mode(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return

            if pygame.mouse.get_pressed()[0]:
                new_point = pygame.mouse.get_pos()
                if self.last_point != new_point:
                    self.drawing_points.append(new_point)
                self.last_point = new_point

            if not pygame.mouse.get_pressed()[0] and len(self.drawing_points) > 0:
                self.is_drawing = False
                return

    def init_callback(self):
        # Begin visualization loop

        dt = 2 * np.pi / len(self.epicycles)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return
                    
            if self.is_drawing:
                self.drawing_mode()
                continue

            self.screen.fill((0, 0, 0))

            self.update_epicycles()

            self.trace_drawing()

            pygame.display.flip()
            self.clock.tick(5000)

            self.time += dt

            if self.time >= 2 * np.pi:
                self.time = 0
                self.end_points.clear()

    def update_epicycles(self):
        # last_center_pos = (self.screen_size / 2).astype(int)
        last_center_pos = (0,0)
        for epicycle in self.epicycles:
            epicycle.update(last_center_pos, self.time)
            last_center_pos = epicycle.dial_end_pos
            epicycle.move()

    def trace_drawing(self):
        self.end_points.append(self.epicycles[-1].dial_end_pos)
        if len(self.end_points) > 1:
            pygame.draw.aalines(self.screen, (50,255,50), False, self.end_points)


class Epicycle(object):
    # Create Epicycle object to store signal data for visualization

    def __init__(self, screen, amp, freq, phase, center_pos):
        self.screen = screen
        
        self.amp = amp
        self.freq = freq
        self.phase = phase
        self.center_pos = center_pos
        
        self.update(self.center_pos, 0)

    def update(self, center_pos, time):
        # Update center and end positions in time

        phi = self.freq * time + self.phase
        
        self.center_pos = center_pos
        self.dial_end_pos = self.center_pos + self.amp * np.array((np.cos(phi), np.sin(phi)))
    
    def move(self):
        radius = 1 if round(self.amp)<1 else int(round(self.amp))
        center = (int(self.center_pos[0]), int(self.center_pos[1]))
        end = (int(self.dial_end_pos[0]), int(self.dial_end_pos[1]))

        self.circle = pygame.draw.circle(self.screen, (255, 255, 255),
                                        center, radius, 1)
        self.line = pygame.draw.line(self.screen, (255, 255, 255),
                                        center, end, 2)

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
