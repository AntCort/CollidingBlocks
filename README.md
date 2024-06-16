# Colliding Blocks Simulation

This is a simple Python simulation that recreates the 'Colliding Simulation' by 3Blue1Brown. It demonstrates the collision and physics interactions between two blocks. One block is stationary while the other moves towards it. Upon collision, the blocks exchange velocities based on their masses, simulating an elastic collision.


## Installation

1. Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install Pygame by running the following command:

## Usage

1. Run `main.py` to start the simulation.

2. The program will open a window showing two blocks. The smaller block is stationary, and the larger block moves towards it.

3. When the blocks collide, they exchange velocities based on their masses, simulating an elastic collision.

4. The simulation will continue running until you close the window.

## Files

- `main.py`: Contains the main program logic, including the Pygame setup and the collision detection algorithm.
- `blocks.py`: Defines the `Blocks` class, which represents the blocks in the simulation.
- `setting.py`: Contains settings such as screen size, block sizes, speeds, colors, and masses.

## Customization

- You can customize the properties of the blocks (size, speed, color, mass) by modifying the constants in `setting.py`.
- Adjust the simulation behavior by modifying the `update_position` method in `blocks.py` or the `detect_collision` function in `main.py`.


## Future Plans

- Add a collision counter to track the number of collisions detected.
- Add a test file (`test.py`) to test the functionality of the simulation.