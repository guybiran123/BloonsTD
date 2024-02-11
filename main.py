import pygame
import sys
import math
from gameplay.game import Game
from gameplay.game_map import GameMap
from utils.constants import *

def calc_angle_to_point(point1, point2):
    print(point1, "\n", point2)
    x1, y1 = point1
    x2, y2 = point2

    # Calculate the differences in coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Use atan2 to calculate the angle
    angle_rad = math.atan2(dy, dx)

    # Convert the angle to degrees
    angle_deg = math.degrees(angle_rad)
    # Ensure the angle is positive
    if angle_deg < 0:
        angle_deg += 360

    return -angle_deg - 90


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotate Example")

# Load an image
image = pygame.image.load(r"C:\Users\guybi\PycharmProjects\BloonsTD\images\Towers\Dart_monkey_image.png")

# Initial rotation angle (in degrees)
angle = 0

# Game loop
running = True
game = Game(Maps.MAP1, 20)
game_map = GameMap(game, screen)
print(game_map.get_route_positions())
while running:
    rotated_image = pygame.transform.rotate(image, angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            angle = calc_angle_to_point((width/2, height/2), pygame.mouse.get_pos())
            print(angle)
    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rotated image
    screen.blit(rotated_image, (width/2 - rotated_image.get_width()/2, height/2 - rotated_image.get_height()/2))

    for position in game_map.get_route_positions():
        pygame.draw.rect(screen, (0, 0, 0), (*position, 1, 1))

    # Update the display
    pygame.display.flip()

    # Increment rotation angle


    # Control the speed of rotation
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
sys.exit()


