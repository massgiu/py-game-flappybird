import pygame


class Utils:

    SCREEN_WIDTH = 288
    SCREEN_HEIGHT = 512
    FPS = 50

    @classmethod
    def initialize(cls):
        # initialize pygame modules
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        return pygame.display.set_mode((Utils.SCREEN_WIDTH, Utils.SCREEN_HEIGHT))

    @classmethod
    def redrawWindow(cls, win, bird):
        background = pygame.image.load("../media/sfondo.png")
        win.blit(background, (0,0))
        win.blit(bird.image, (bird.x, bird.y))
        pygame.display.update()  # Updates the screen
        pygame.time.Clock().tick(Utils.FPS)




