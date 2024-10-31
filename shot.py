import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)

        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOOT_SPEED

        if hasattr(self, "containers"):
            self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt