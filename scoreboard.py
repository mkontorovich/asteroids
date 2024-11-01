import pygame
from constants import *
import json
import database

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
        self.highest_score = self.load_highest_score()

    def increase_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def draw_high_score(self, screen):
        score_text = self.font.render(f"High Score: {self.highest_score}", True, self.color)
        screen.blit(score_text, self.high_score_position)

    def draw_current_score(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, self.current_score_position)

    def save_score(self):
        database.add_high_score("Player1", self.score)

    def load_highest_score(self):
        highest_score = database.get_top_scores()
        if highest_score: # Check if there is at least one entry
            # Get the score from the first entry (which is the highest score)
            return int(highest_score[1]) # The score is in the second column
        return 0
