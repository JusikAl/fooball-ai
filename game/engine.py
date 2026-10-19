import pygame
import sys

from game.pitch import Pitch
from game.ball import Ball
from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.pitch = Pitch(self.screen)
        self.ball = Ball(self.screen)
        
    def run(self):
        while True:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.ball.update()
            self.pitch.draw()
            self.ball.draw()
            
            pygame.display.flip()