import pygame
from src.Utils import Utils
from src.Bird import Bird
from src.Base import Base

#clock = pygame.time.Clock()  # create an object to help track time

def main():

    win = Utils.initialize()

    pipe_down = pygame.image.load("../media/tubo.png")
    # vertical transform True, horizontal transform false
    pipe_up = pygame.transform.flip(pipe_down, False, True)

    bird = Bird()
    base = Base()
    while True:
        #pygame.time.delay(50)  # if increases, then goes quicker
        bird.move(win)
        base.move()
        Utils.redrawWindow(win, bird, base)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
