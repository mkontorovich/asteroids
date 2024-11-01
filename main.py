import pygame
from constants import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *
import sys
from scoreboard import *
from sound_manager import *
import database

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Load the Asteroids image
    icon = pygame.image.load('assets/asteroids_logo.png')
    database.create_table()

    pygame.init()
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_color = SCREEN_BG_COLOR
    
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
    sound_manager = SoundManager()

    last_shot_time = 0
    bullet_cooldown = BULLET_COOLDOWN

    game_running = True
    while (game_running):
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks() / 1000
                    if current_time - last_shot_time >= bullet_cooldown:  # Check if cooldown is over
                        sound_manager.play_bullet_sound()
                        last_shot_time = current_time

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
                print(database.print_scores())
                sys.exit()

        screen.fill(bg_color)
        
        for item in drawable:
            item.draw(screen)

        scoreboard.draw_high_score(screen)
        scoreboard.draw_current_score(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
