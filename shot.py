import pygame
from circleshape import *
from constants import *
from sound_manager import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

        if hasattr(self, "containers"):
            self.add(*self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, SHOT_COLOR, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

        # kill bullets that go off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
                self.kill()