import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000000) # setting screen to black
        pygame.display.flip() # updates display

        dt = clock.tick(60) / 1000 # limits framerate to 60 fps

if __name__ == "__main__":
    main()
