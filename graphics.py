import numpy as np

import pygame


class Graphics(object):
    # Class to hold PyGame visualization data

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
