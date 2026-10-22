import pygame 

from config import BALL_RADIUS

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(500, 400)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = BALL_RADIUS
        self.kick_speed = 8 
        
    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self):
        self.position += self.velocity
        self.velocity *= 0.98
        if self.velocity.length() <= 0.1:
            self.velocity = pygame.Vector2(0, 0)
        
    def bounce_from(self, player_position):
        direction = self.position - player_position

        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.velocity = direction * self.kick_speed