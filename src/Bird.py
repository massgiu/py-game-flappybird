import pygame, sys
from src.Constants import Constants

class Bird:

    def __init__(self):
        self.reset_pos()
        self.image = pygame.image.load("../media/bird.png")
        self.img_rect = self.image.get_rect()

    def reset_pos(self):
        self.x = Constants.BIRD_INITIAL_X
        self.y = Constants.BIRD_INITIAL_Y
        self.speedy = 0

    def move(self, win):
        # Gestore di eventi: intercetto eventi tastiera
        #self.speedy += 1 #aumento velocità verticale
        #self.y += self.speedy #mi sposto verso il basso sempre più rapidamente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    #pass
                    self.x -= Constants.BIRD_INCREMENT
                elif keys[pygame.K_RIGHT]:
                    #pass
                    self.x+= Constants.BIRD_INCREMENT
                elif keys[pygame.K_DOWN]:
                    #pass
                    self.y += Constants.BIRD_INCREMENT
                elif keys[pygame.K_UP]:
                    #self.speedy = -10 #rallenta la discesa
                    self.y -= Constants.BIRD_INCREMENT
                    #pass

    def is_too_low(self):
        return self.y >Constants.DANGEROUS_HEIGHT