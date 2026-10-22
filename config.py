import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

PITCH_SIZE = (900, 700)

BALL_RADIUS = 10

RED_TEAM_COLOR = (255, 0, 0)
BLUE_TEAM_COLOR = (0, 0, 255)
PLAYER_RADIUS = 20
PLAYER_SPEED = 5

RED_CONTROLS = {
    "up" : pygame.K_UP,
    "down" : pygame.K_DOWN,
    "right" : pygame.K_RIGHT,
    "left" : pygame.K_LEFT,
}

BLUE_CONTROLS = {
    "up" : pygame.K_w,
    "down" : pygame.K_s,
    "left" : pygame.K_a,
    "right" : pygame.K_d
}