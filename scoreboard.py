import pygame
from constants import *
import json

class ScoreBoard():
    def __init__(self, 
                 font_path=SCOREBOARD_FONT_FILE,
                 font_size=SCOREBOARD_FONT_SIZE, 
                 color=SCOREBOARD_COLOR, 
                 high_score_position=SCOREBOARD_HIGH_SCORE_POSITION,
                 current_score_position=SCOREBOARD_CURRENT_SCORE_POSITION,
                 score_file=SCOREBOARD_FILE):
        self.score = 0
        self.color = color
        self.high_score_position = high_score_position
        self.current_score_position = current_score_position
        self.font = pygame.font.Font(font_path, font_size)
        self.score_file = score_file
        self.high_scores = self.load_high_score()

    def increase_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def draw_high_score(self, screen):
        score_text = self.font.render(f"High Score: {self.high_scores}", True, self.color)
        screen.blit(score_text, self.high_score_position)

    def draw_current_score(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, self.current_score_position)

    def save_score(self):
        if self.score > self.high_scores:
            self.high_scores = self.score
            with open(self.score_file, 'w') as file:
                json.dump({"high_score": self.high_scores}, file)

    def load_high_score(self):
        try:
            with open(self.score_file, 'r') as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0