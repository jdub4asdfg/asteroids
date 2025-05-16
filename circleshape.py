import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Sub-classes will override
        pass

    def update(self, dt):
        # Sub-classes will override
        pass

    def collision_check(self, other):
        # Calculates euclidean distance between centres of 2 objects
        distance = pygame.Vector2.distance_to(self.position, other.position)

        # If the euclidean distance is less than or equal to the 2 objects' radii combined, they are colliding
        if (distance <= (self.radius + other.radius)):
            return True
        else:
            return False
