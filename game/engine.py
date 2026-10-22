import pygame
import sys

from game.pitch import Pitch
from game.ball import Ball
from game.rules import Rules
from config import (FPS, 
                    SCREEN_HEIGHT, SCREEN_WIDTH, 
                    RED_TEAM_COLOR, BLUE_TEAM_COLOR, 
                    RED_CONTROLS, BLUE_CONTROLS)
from game.player import Player

pygame.init()

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.pitch = Pitch(self.screen)
        self.ball = Ball(self.screen)
        self.rules = Rules()
        self.player1 = Player(self.screen, (200, 400), BLUE_TEAM_COLOR, BLUE_CONTROLS)
        self.player2 = Player(self.screen, (800, 400), RED_TEAM_COLOR, RED_CONTROLS)
        
    def run(self):
        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            distance = self.player1.position.distance_to(self.ball.position)
            
            if distance <= self.player1.player_radius + self.ball.radius:
                self.ball.bounce_from(self.player1.position)
            
            self.ball.update()
            self.rules.check_out(self.ball.position)
            self.pitch.draw()
            self.ball.draw()
            self.player1.update()
            self.player1.draw_player()
            self.player2.update()
            self.player2.draw_player()
            
            pygame.display.flip()