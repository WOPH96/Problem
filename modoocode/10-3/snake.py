import pygame
from pygame.locals import *
import random
import sys
import time

pygame.init()

# Set up window and game display
window_width = 640
window_height = 960
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Define colors for the snake and food
snakeColor = (255, 0, 0) # red
foodColor = (0, 255, 0) # green

snakeX=0
snakeY=0

# Set up game loop
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == KEYDOWN and event.key == K_LEFT: # move left
            snakeX -= 5
            
        elif event.type == KEYDOWN and event.key == K_RIGHT: # move right
            snakeX += 5
        
        elif event.type == KEYDOWN and event.key == K_UP: # move up
            snakeY -= 5
            
        elif event.type == KEYDOWN and event.key == K_DOWN: # move down
            snakeY += 5
    
    # Move food to a random location on the screen
    foodX = round(random.randint(10, window_width - 10))
    foodY = round(random.randint(10, window_height - 10))

    # Draw game objects on the screen
    pygame.draw.rect(gameDisplay, snakeColor, (snakeX, snakeY, 25, 25)) # draw snake
    pygame.draw.rect(gameDisplay, foodColor, (foodX, foodY, 25, 25)) # draw food
    
    # Update game display
    pygame.display.update()

pygame.quit()