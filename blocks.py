import pygame

# Create class for Block creation
class Blocks:
    def __init__(self, surface, x_pos, y_pos, size, speed, color, mass):
        self.surface = surface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.speed = speed
        self.mass = mass # KG
        self.color = color
    
    
    # Draws the block 
    def draw_block(self):
        pygame.draw.rect(self.surface, self.color, (self.x_pos, self.y_pos, self.size, self.size))
    
    # Use to give the first block a 'push' to the left at the beginning of the program 
    def update_position(self):
        self.x_pos += - self.speed
    
    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)
    
    def get_pos(self):
        return self.x_pos

        
                

        