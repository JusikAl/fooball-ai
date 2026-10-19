import pygame 

from config import BALL_RADIUS

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(500, 400)
        self.velocity = pygame.Vector2(3, 2)
        self.radius = BALL_RADIUS
        
    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self):
        self.position += self.velocity