import pygame


class Bird:

    def __init__(self):
        self.x = 60
        self.y = 150
        self.speedy = 0
        self.image = pygame.image.load("../media/bird.png")

    def move(self):
        # Gestore di eventi: intercetto eventi tastiera
        self.speedy += 1 #aumento velocità verticale
        self.y += self.speedy #mi sposto verso il basso sempre più rapidamente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    pass
                elif keys[pygame.K_RIGHT]:
                    pass
                elif keys[pygame.K_DOWN]:
                    pass
                elif keys[pygame.K_UP]:
                    self.speedy = -10 #rallenta la discesa