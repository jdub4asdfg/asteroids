import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x, y) # creating a player object
    asteroidfield = AsteroidField() # creating the asteroid field

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000000) # setting screen to black

        for object in drawable:
            object.draw(screen)

        updatable.update(dt)

        for object in asteroids:
           if object.collision_check(player):
                sys.exit("Game over!")

        pygame.display.flip() # updates display

        dt = clock.tick(60) / 1000 # limits framerate to 60 fps

if __name__ == "__main__":
    main()
