import pygame

from config import PITCH_SIZE

class Pitch:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        self.screen.fill((0, 128, 0))  # Fill the screen with green color
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, PITCH_SIZE[0], PITCH_SIZE[1]), 5)  # Draw the pitch boundary
        pygame.draw.line(self.screen, (255, 255, 255), (500, 50), (500, 750), 5)  # Draw the center line
        pygame.draw.circle(self.screen, (255, 255, 255), (500, 400), 75, 5)  # Draw the center circle
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 275, 200, 250), 5)  # Draw the left penalty area
        pygame.draw.rect(self.screen, (255, 255, 255), (750, 275, 200, 250), 5)  # Draw the right penalty area
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 350, 50, 100), 5)  # Draw the left goal
        pygame.draw.rect(self.screen, (255, 255, 255), (900, 350, 50, 100), 5)  # Draw the right goal
        pygame.draw.circle(self.screen, (255, 255, 255), (150, 400), 10, 5) # Draw left penalty spot
        pygame.draw.circle(self.screen, (255, 255, 255), (850, 400), 10, 5) # Draw right penalty spot