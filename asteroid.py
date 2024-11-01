import pygame
from constants import *
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if hasattr(self, "containers"):
            self.add(*self.containers)

        self.velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2

            split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            split_asteroid1.velocity = velocity1
            split_asteroid2.velocity = velocity2