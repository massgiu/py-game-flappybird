import random
import pygame
from src.Constants import Constants

class Pipe:

    def __init__(self):
        self.x = 300 #Initial value is 300 (out of screen)
        self.y = random.randint(-75,150)
        self.pipe_down = pygame.image.load("../media/pipe.png")
        # vertical transform True, horizontal transform false
        self.pipe_up = pygame.transform.flip(self.pipe_down, False, True)

    def move(self):
        self.x -= Constants.INITIAL_SPEED
        self.pipe_down_y = self.y + Constants.PIPE_HOLE
        self.pipe_up_y = self.y - Constants.PIPE_HOLE