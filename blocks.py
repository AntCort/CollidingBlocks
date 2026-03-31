import pygame


class Block:
    def __init__(self, surface, x_pos, y_pos, size, speed, color, mass):
        self.surface = surface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.speed = speed
        self.color = color
        self.mass = mass

    def draw(self):
        pygame.draw.rect(
            self.surface,
            self.color,
            (self.x_pos, self.y_pos, self.size, self.size),
        )

    def move(self):
        # Subtract speed so positive values move the block left.
        self.x_pos -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x_pos, self.y_pos, self.size, self.size)

    def get_pos(self):
        return self.x_pos