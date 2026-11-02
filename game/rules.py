import pygame

from config import BALL_RADIUS, PLAYER_RADIUS, LEFT, RIGHT, BOTTOM, TOP

class Rules:
    def __init__(self, ball):
        self.ball = ball

    
    def check_out(self):
        in_goal_mouth = 350 <= self.ball.position.y <= 450
        if in_goal_mouth and (self.ball.position.x - BALL_RADIUS <= LEFT
                            or self.ball.position.x + BALL_RADIUS >= RIGHT):
            return
        if (self.ball.position.x - BALL_RADIUS < LEFT
            or self.ball.position.x + BALL_RADIUS > RIGHT
            or self.ball.position.y - BALL_RADIUS < TOP
            or self.ball.position.y + BALL_RADIUS > BOTTOM):
            self.reset_ball()
    
    @staticmethod
    def player_out(player_pos):
        if player_pos.x - PLAYER_RADIUS < 50 or player_pos.x + PLAYER_RADIUS > 950 or player_pos.y - PLAYER_RADIUS < 50 or player_pos.y + PLAYER_RADIUS > 750:
            return True
        return False
    
    def check_goal(self):
        if self.ball.position.x + self.ball.radius >= RIGHT and 350 <= self.ball.position.y <= 450:
            return "Blue"

        if self.ball.position.x - self.ball.radius <= LEFT and 350 <= self.ball.position.y <= 450:
            return "Red"

        return None
    
    def reset_ball(self):
        self.ball.position = pygame.Vector2(500, 400)
        self.ball.velocity = pygame.Vector2(0, 0)