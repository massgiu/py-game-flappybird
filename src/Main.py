from src.Bird import Bird
from src.Ground import Ground
from src.Pipe import Pipe
from src.Utils import Utils
from src.Constants import Constants
import pygame

#clock = pygame.time.Clock()  # create an object to help track time

def main():

    win = Utils.initialize()
    clock = pygame.time.Clock()

    bird = Bird()
    ground = Ground()
    pipe_list = [Pipe()]
    while True:
        clock.tick(Constants.FPS) # Now your game will be capped at FPS fps
        bird.move(win)
        ground.move()
        Utils.move_pipe_list(pipe_list)
        pipe_list = Utils.check_collision(win, bird, ground, pipe_list)
        Utils.redrawWindow(win, bird, ground, pipe_list)

if __name__ == '__main__':
    main()
