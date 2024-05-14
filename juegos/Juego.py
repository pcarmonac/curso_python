import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Ball
ball_radius = 10
ball_speed = 5
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_direction_x = -1
ball_direction_y = 1
