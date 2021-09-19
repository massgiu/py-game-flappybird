from src.Bird import Bird
from src.Ground import Ground
from src.PipeList import PipeList
from src.Utils import Utils
from src.Constants import Constants
import pygame

#clock = pygame.time.Clock()  # create an object to help track time

def main():

    win = Utils.initialize()
    clock = pygame.time.Clock()

    bird = Bird()
    ground = Ground()
    pipes = PipeList()
    while True:
        clock.tick(Constants.FPS) # Now your game will be capped at FPS fps
        bird.move(win)
        ground.move()
        pipes.move()
        Utils.check_collision(win, bird, ground, pipes)
        Utils.redrawWindow(win, bird, ground, pipes)

if __name__ == '__main__':
    main()
