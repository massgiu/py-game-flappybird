import pygame, sys
from src.Pipe import Pipe
from src.Constants import Constants

class Utils:

    @classmethod
    def initialize(cls):
        # initialize pygame modules
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        return pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    @classmethod
    def redrawWindow(cls, win, bird, ground, pipe_list):
        background = pygame.image.load("../media/background.png")
        win.blit(background, (0,0))
        win.blit(ground.image, (ground.x, ground.y))
        for p in pipe_list:
            win.blit(p.pipe_up, (p.x, p.pipe_up_y))
            win.blit(p.pipe_down, (p.x, p.pipe_down_y))
        if pipe_list[-1].x+pipe_list[-1].pipe_down.get_width() < bird.x:
            pipe_list.append(Pipe())
        if (bird.is_too_low()):
            Utils.you_lost(win, bird, ground)
        else:
            win.blit(bird.image, (bird.x, bird.y))
        pygame.display.update()  # Updates the screen

    @classmethod
    def restart(cls, bird, ground):
        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                for key in keys:
                    if keys[pygame.K_SPACE]:
                        bird.reset_pos()
                        ground.reset_pos()
                        restart = True
    @classmethod
    def you_lost(cls, win, bird, ground):
        win.blit(pygame.image.load("../media/gameover.png"), (50, 180))
        pygame.display.update()
        Utils.restart(bird, ground)

    @classmethod
    def move_pipe_list(cls, pipe_list):
        for elem in pipe_list:
            elem.move()

    @classmethod
    def check_collision(cls, win, bird, ground, pipe_list):
        for p in pipe_list:
            right_dist_bird = bird.x + bird.image.get_width()
            right_dist_pipe = p.x + p.pipe_up.get_width()
            up_dist_bird = bird.y
            down_dist_bird = bird.y + bird.image.get_height()
            left_dist_pipe = p.x
            up_dist_pipe = p.pipe_up_y + p.pipe_up.get_height()
            down_dist_pipe = p.pipe_down_y
            if right_dist_pipe < bird.x: #bird overtake pipe
                print("overtaken")
                if right_dist_pipe<0: #remove pipe from list
                    pipe_list.remove(p)
                    print("Deleted pipe")
            else:
                #print(f"Down side pipe {down_side_pipe}")
                #print(f"Up side pipe {up_side_pipe}")
                if right_dist_bird>left_dist_pipe:
                    print("overlapping x")
                    if up_dist_bird<up_dist_pipe or down_dist_bird>down_dist_pipe:
                        print("pipe overlapping")
                        Utils.you_lost(win, bird, ground)
                        pipe_list = [pipe_list[-1]] #keep last pipe
            return pipe_list
