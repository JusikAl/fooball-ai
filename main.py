import pygame
import sys

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from game.engine import GameEngine

pygame.init()

game_engine = GameEngine()
game_engine.run()
            
