import pygame

from config import BALL_RADIUS, PLAYER_RADIUS

class Rules:
    def __init__(self, ball):
        self.ball = ball
        pass
    
    def check_out(self):
        if self.ball.position.x - BALL_RADIUS < 50 or self.ball.position.x + BALL_RADIUS > 950 or self.ball.position.y - BALL_RADIUS < 50 or self.ball.position.y + BALL_RADIUS > 750:
            self.ball.position = pygame.Vector2(500, 400)
            self.ball.velocity = pygame.Vector2(0, 0)
    
    @staticmethod
    def player_out(player_pos):
        if player_pos.x - PLAYER_RADIUS < 50 or player_pos.x + PLAYER_RADIUS > 950 or player_pos.y - PLAYER_RADIUS < 50 or player_pos.y + PLAYER_RADIUS > 750:
            return True
        return False