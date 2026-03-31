from blocks import Block
from settings import (
    BLOCK_ONE_X,
    BLOCK_ONE_Y,
    BLOCK_ONE_SIZE,
    BLOCK_ONE_SPEED,
    BLOCK_ONE_COLOR,
    BLOCK_ONE_MASS,
    BLOCK_TWO_X,
    BLOCK_TWO_Y,
    BLOCK_TWO_SIZE,
    BLOCK_TWO_SPEED,
    BLOCK_TWO_COLOR,
    BLOCK_TWO_MASS,
)


def create_blocks(screen):
    block_1 = Block(
        surface=screen,
        x_pos=BLOCK_ONE_X,
        y_pos=BLOCK_ONE_Y,
        size=BLOCK_ONE_SIZE,
        speed=BLOCK_ONE_SPEED,
        color=BLOCK_ONE_COLOR,
        mass=BLOCK_ONE_MASS,
    )

    block_2 = Block(
        surface=screen,
        x_pos=BLOCK_TWO_X,
        y_pos=BLOCK_TWO_Y,
        size=BLOCK_TWO_SIZE,
        speed=BLOCK_TWO_SPEED,
        color=BLOCK_TWO_COLOR,
        mass=BLOCK_TWO_MASS,
    )

    return block_1, block_2


def detect_collision(block1, block2, collision_count):
    rect1 = block1.get_rect()
    rect2 = block2.get_rect()

    if rect1.colliderect(rect2):
        b1_speed, b2_speed = block1.speed, block2.speed
        b1_mass, b2_mass = block1.mass, block2.mass

        vel_1 = ((b1_mass - b2_mass) * b1_speed + 2 * b2_mass * b2_speed) / (b1_mass + b2_mass)
        vel_2 = ((b2_mass - b1_mass) * b2_speed + 2 * b1_mass * b1_speed) / (b1_mass + b2_mass)

        block1.speed = vel_1
        block2.speed = vel_2
        collision_count += 1

        # Push blocks apart so the same collision is not counted multiple times.
        overlap = rect1.right - rect2.left
        if overlap > 0:
            block1.x_pos -= overlap / 2
            block2.x_pos += overlap / 2

    if block1.get_pos() <= 0:
        block1.x_pos = 0
        block1.speed = -block1.speed
        collision_count += 1

    if block2.get_pos() <= 0:
        block2.x_pos = 0
        block2.speed = -block2.speed
        collision_count += 1

    return collision_count