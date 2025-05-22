import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Removes the asteroid that was shot
        self.kill()

        # If asteroid is small, don't split else...
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Calculating the angle at which the smaller asteroids will split from its parent
            random_angle = random.uniform(20, 50)

            # Calculating the velocity of the smaller asteroids with parents speed (not final) and the angle
            first_vector = pygame.Vector2.rotate(self.velocity, random_angle)
            second_vector = pygame.Vector2.rotate(
                self.velocity, -(random_angle))

            new_asteroid_radii = self.radius - ASTEROID_MIN_RADIUS

            # Creating the smaller asteroids
            new_asteroid_1 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radii
            )
            new_asteroid_2 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radii
            )

            # Setting their speed to be faster (final)
            new_asteroid_1.velocity = first_vector * 1.2
            new_asteroid_2.velocity = second_vector * 1.2
