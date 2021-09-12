import pygame
from src.Utils import Utils
from src.Bird import Bird

#clock = pygame.time.Clock()  # create an object to help track time

# player = Player(Utils.init_pos_x, Utils.init_pos_y, Utils.charact_width, Utils.charact_height)
# enemy = Enemy(Utils.enemy_init_pos_x, Utils.enemy_init_pos_y, Utils.enemy_width, Utils.enemy_height, Utils.screen_width - 150)

def main():

    win = Utils.initialize()

    base = pygame.image.load("../media/base.png")
    pipe_down = pygame.image.load("../media/tubo.png")
    # vertical transform True, horizontal transform false
    pipe_up = pygame.transform.flip(pipe_down, False, True)

    bird = Bird()
    while True:
        #pygame.time.delay(50)  # if increases, then goes quicker
        bird.move()
        Utils.redrawWindow(win, bird)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
