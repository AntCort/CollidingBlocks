import sys
import pygame

from physics import create_blocks, detect_collision
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from ui import show_collision_count, draw_track


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Colliding Blocks")

    collision_font = pygame.font.Font("freesansbold.ttf", 32)
    collision_count = 0

    block_1, block_2 = create_blocks(screen)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    collision_count = 0
                    block_1, block_2 = create_blocks(screen)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BACKGROUND_COLOR)
        show_collision_count(screen, collision_font, collision_count)
        draw_track(screen)

        block_1.move()
        block_2.move()

        block_1.draw()
        block_2.draw()

        collision_count = detect_collision(block_1, block_2, collision_count)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()