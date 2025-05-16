import pygame
import sys

from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Packaging all objects into groups so that they are easier and more concise to reference (AFAIK it's just a pygame thing)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Creating a player object
    player = Player(x, y)

    # Creating an asteroid field
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Where the packages come in handy
        for object in drawable:
            object.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                sys.exit("Game over!")

            for bullet in shots:
                if bullet.collision_check(asteroid):
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()

        # Limits framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
