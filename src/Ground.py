import pygame
from src.Constants import Constants

class Ground:

    def __init__(self):
        self.reset_pos()
        self.image =  pygame.image.load("../media/ground.png")

    def reset_pos(self):
        self.x = 0
        self.y = 400
        self.speedx = Constants.INITIAL_SPEED

    def move(self):
        self.x -= self.speedx  # mi sposto vers sx
        #replico la base
        if self.x < -45:
            self.x = 0