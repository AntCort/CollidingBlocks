import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, TRACK_COLOR, TEXT_COLOR


def show_collision_count(screen, font, collision_count):
    count_surface = font.render(
        f"Count: {collision_count}",
        True,
        TEXT_COLOR,
    )
    screen.blit(count_surface, (10, 10))


def draw_track(screen):
    pygame.draw.line(
        screen,
        TRACK_COLOR,
        start_pos=(0, SCREEN_HEIGHT // 2),
        end_pos=(SCREEN_WIDTH, SCREEN_HEIGHT // 2),
        width=5,
    )