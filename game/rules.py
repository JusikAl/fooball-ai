import pygame

from config import BALL_RADIUS

class Rules:
    def __init__(self):
        pass
    
    def check_out(self, ball_position):
        if ball_position.x + BALL_RADIUS < 50 or ball_position.x - BALL_RADIUS > 950 or ball_position.y + BALL_RADIUS < 50 or ball_position.y - BALL_RADIUS > 750:
            pass