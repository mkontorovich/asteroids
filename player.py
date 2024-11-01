from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Call superclass constructor
        self.rotation = 0
        self.shoot_timer = 0

        if Player.containers:  # Access the containers directly from the class
            Player.containers[0].add(self)  # Add to updatable
            Player.containers[1].add(self)  # Add to drawable

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def shoot(self):
        if self.shoot_timer <= 0:  # Allow shooting only if the timer has expired
            shot_position = pygame.Vector2(self.position)
            shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  # Correctly calculate velocity
            shot = Shot(shot_position.x, shot_position.y, shot_velocity)  # Create the shot instance
            
            # Add the shot to the relevant containers if it exists
            if hasattr(Shot, "containers"):
                for container in Shot.containers:
                    container.add(shot)  # Add shot to containers

            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer after shooting
