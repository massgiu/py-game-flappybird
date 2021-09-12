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
    def redrawWindow(cls, win, bird, base):
        background = pygame.image.load("../media/sfondo.png")
        win.blit(background, (0,0))
        win.blit(base.image, (base.x, base.y))
        if (bird.have_you_lost()):
            win.blit(bird.gameover, (50, 180))
            Utils.restart(bird,base)
        else:
            win.blit(bird.image, (bird.x, bird.y))
        pygame.display.update()  # Updates the screen
        pygame.time.Clock().tick(Utils.FPS)

    @classmethod
    def restart(cls,bird,base):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_SPACE]:
                    print("Spazio")
                    bird.reset_pos()
                    base.reset_pos()





