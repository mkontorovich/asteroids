import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys
from scoreboard import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Load the Asteroids image
    icon = pygame.image.load('assets/asteroids_logo.png')

    pygame.init()
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_color = constants.SCREEN_BG_COLOR
    
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y) # player is in the center
    asteroid_field = AsteroidField() # draws the asteroid field, so we can see asteroids
    scoreboard = ScoreBoard() # draws the scoreboard, so we can see our score

    game_running = True
    while (game_running):
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
                    scoreboard.increase_score(1)

            if player.collision_check(asteroid):
                print("Game Over!")
                scoreboard.save_score()
                scoreboard.reset_score()
                sys.exit()

        screen.fill(bg_color)
        
        for item in drawable:
            item.draw(screen)

        scoreboard.draw_high_score(screen)
        scoreboard.draw_current_score(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
