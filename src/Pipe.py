import random
import pygame
from src.Constants import Constants

class Pipe:

    count = 0
    speed = Constants.INITIAL_SPEED

    def __init__(self):
        self.x = 300 #Initial value is 300 (out of screen)
        self.y = random.randint(-75,150)
        self.pipe_down = pygame.image.load("../media/pipe.png")
        # vertical transform True, horizontal transform false
        self.pipe_up = pygame.transform.flip(self.pipe_down, False, True)
        self.pipe_down_y = self.y + Constants.PIPE_HOLE
        self.pipe_up_y = self.y - Constants.PIPE_HOLE

    @classmethod
    def count_pipe(cls):
        cls.count+=1

    @classmethod
    def reset(cls):
        cls.count = 0
        cls.speed = Constants.INITIAL_SPEED

    def move(self):
        if self.count>0 and self.count%5==0:
            Pipe.speed += Constants.SPEED_INCREMENT
        self.x -= Pipe.speed