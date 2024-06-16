import pygame
import sys
from setting import *
from blocks import Blocks

# Initialize Pygame
pygame.init()

# Setting up a simple window that will appear once the program is ran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Colliding Blocks')

# Creating first block
block_1 = Blocks(surface=screen, x_pos=BLOCK_ONE_X, y_pos=BLOCK_ONE_Y, size=BLOCK_ONE_SIZE, speed=BLOCK_ONE_SPEED, color=BLOCK_ONE_COLOR, mass=BLOCK_ONE_MASS)
block_2 = Blocks(surface=screen, x_pos=BLOCK_TWO_X, y_pos=BLOCK_TWO_Y, size=BLOCK_TWO_SIZE, speed=BLOCK_TWO_SPEED, color=BLOCK_TWO_COLOR, mass=BLOCK_TWO_MASS)

# Checks if the blocks collide
def detect_collision(block1, block2):
    
    if block1.get_rect().colliderect(block2.get_rect()):
        # Elastic collision equations
        b1_speed, b2_speed = block1.speed, block2.speed
        b1_mass, b2_mass = block1.mass, block2.mass

        vel_1 = ((b1_mass - b2_mass) * b1_speed + 2 * b2_mass * b2_speed) / (b1_mass + b2_mass)
        vel_2 = ((b2_mass - b1_mass) * b2_speed + 2 * b1_mass * b1_speed) / (b1_mass + b2_mass)

        block1.speed = vel_1
        block2.speed = vel_2

    # Checks if block 1 is out of bounds
    if block1.get_pos() <= 0:
        block1.speed = -block1.speed
    # Checks if block 2 is out of bounds
    if block2.get_pos() <= 0:
        block2.speed = -block2.speed
    
    
# Will keep running until user 'quits' program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Drawing the line the cubes will run on
    pygame.draw.line(screen, 'gray', start_pos=(0, SCREEN_HEIGHT // 2), end_pos=(SCREEN_WIDTH, SCREEN_HEIGHT // 2), width=5)  # Horizontal line

    # Updates positions for both blocks
    block_1.update_position()
    block_2.update_position()
    
    # Drawing blocks
    block_1.draw_block()
    block_2.draw_block()
    
    detect_collision(block_1, block_2)

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Control frame rate to 60 FPS

pygame.quit()
sys.exit()
