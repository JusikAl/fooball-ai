import pygame

from config import BALL_RADIUS, PLAYER_RADIUS

class Rules:
    def __init__(self):
        pass
    
    def check_out(self, ball_position):
        if ball_position.x - BALL_RADIUS < 50 or ball_position.x + BALL_RADIUS > 950 or ball_position.y - BALL_RADIUS < 50 or ball_position.y + BALL_RADIUS > 750:
            ball_position = pygame.Vector2(500, 400)
        
    def player_out(self, player_pos):
        if player_pos.x - PLAYER_RADIUS < 50 or player_pos.x + PLAYER_RADIUS > 950 or player_pos.y - PLAYER_RADIUS < 50 or player_pos.y + PLAYER_RADIUS > 750:
            return True
        return False