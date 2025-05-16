import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite): #using pygame to create a circle for us
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes will override
        pass

    def update(self, dt):
        # sub-classes will override
        pass

    def collision_check(self, other):
        distance = pygame.Vector2.distance_to(self.position, other.position)

        if (distance <= (self.radius + other.radius)):
            return True
        else:
            return False
