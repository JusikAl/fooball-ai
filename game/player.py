import pygame
from pygame import key

from config import PLAYER_RADIUS, PLAYER_SPEED, RED_CONTROLS, BLUE_CONTROLS 
from game.rules import Rules

class Player:
    
    def __init__(self, screen, start_position, player_color, controls):
        self.screen = screen
        self.position = pygame.Vector2(start_position)
        self.player_radius = PLAYER_RADIUS
        self.speed = PLAYER_SPEED
        self.controls = controls
        self.player_color = player_color
        self.rules = Rules()
        
    def draw_player(self):
        pygame.draw.circle(self.screen, self.player_color, self.position, self.player_radius)
    
    def update(self):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)
        
        if keys[self.controls["left"]]:
            direction.x -= 1
        if keys[self.controls["right"]]:
            direction.x += 1 
        if keys[self.controls["up"]]:
            direction.y -= 1
        if keys[self.controls["down"]]:
            direction.y += 1
            
        if direction.length() > 0:
            direction = direction.normalize()
        
        
        new_position = self.position.copy()
        
        new_position += direction * self.speed
        
        if not self.rules.player_out(new_position):
            self.position = new_position
            
        