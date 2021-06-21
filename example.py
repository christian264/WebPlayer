import cv2
import numpy as n
from random import randint
from WebPlayer import WebPlayer

import pygame as pygame


displayIO = WebPlayer(pygame)
screen = displayIO.display

running = True
v=0
while running:
    screen.fill((0, 255, randint(0,255)))
    # event = pygame.event.poll()
    # if event.type == pygame.QUIT:
    #     running = 0
    v += 0.1

    if displayIO.mouse:
        # print(((int(displayIO.mouse_x),int(displayIO.mouse_y)),(int(displayIO.mouse_x+100),int(displayIO.mouse_y+200))))
        pygame.draw.rect(screen, 255, ((int(displayIO.mouse_x),int(displayIO.mouse_y)),(int(100),int(100))))
    # pygame.draw.rect(screen, 255, ((int(13),25),(235,242)))


    pygame.display.update()

    pygame.display.flip()


