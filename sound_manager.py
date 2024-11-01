import pygame

class SoundManager():
    def __init__(self):
        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound("assets/sounds/bullet.wav")

    def play_bullet_sound(self):
        self.bullet_sound.play()