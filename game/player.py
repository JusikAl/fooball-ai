import pygame
from pygame import key

from config import PLAYER_RADIUS, PLAYER_SPEED, BLUE_TEAM_COLOR
from game.rules import Rules

class Player:
    
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(200, 200)
        self.player_radius = PLAYER_RADIUS
        self.speed = PLAYER_SPEED
        self.player_team_blue = BLUE_TEAM_COLOR
        self.rules = Rules()
        
    def draw_player(self):
        pygame.draw.circle(self.screen, self.player_team_blue, self.position, self.player_radius)
    
    def update(self):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)
        
        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1
            
        if direction.length() > 0:
            direction = direction.normalize()
        
        
        new_position = self.position.copy()
        
        new_position += direction * self.speed
        
        if not self.rules.player_out(new_position):
            self.position = new_position