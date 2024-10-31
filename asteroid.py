import pygame
import constants
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Correctly pass x, y, and radius to CircleShape

        if hasattr(self, "containers"):
            self.add(*self.containers)

        self.velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))

    def draw(self, screen):
        pygame.draw.circle(screen, constants.ASTEROID_COLOR, (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt