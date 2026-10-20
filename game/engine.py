import pygame
import sys

from game.pitch import Pitch
from game.ball import Ball
from game.rules import Rules
from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player

pygame.init()

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.pitch = Pitch(self.screen)
        self.ball = Ball(self.screen)
        self.rules = Rules()
        self.player = Player(self.screen)
        
    def run(self):
        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.ball.update()
            self.rules.check_out(self.ball.position)
            self.pitch.draw()
            self.ball.draw()
            self.player.update()
            self.player.draw_player()
            self.rules.player_out(self.player.position)
            
            pygame.display.flip()