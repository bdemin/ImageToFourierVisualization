import numpy as np

import pygame


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
