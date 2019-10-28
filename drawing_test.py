
import numpy as np

import pygame


pygame.init()
screen_size = np.array((1200, 800))
screen = pygame.display.set_mode(screen_size, 0, 32)

mouse = pygame.mouse
points = []
last_point = (0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    if mouse.get_pressed()[0]:
        new_point = mouse.get_pos()
        if last_point != new_point:
            points.append(new_point)
        last_point = new_point

    screen.fill((0, 0, 0))

    pygame.display.flip()
