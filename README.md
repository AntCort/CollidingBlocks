# Colliding Blocks Simulation

A simple Python and Pygame simulation inspired by 3Blue1Brown’s colliding blocks example. The program models elastic collisions between two blocks with different masses and displays a collision counter in real time.

## Installation

1. Create and activate a virtual environment  
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Controls

- `R` → Reset simulation  
- `ESC` → Exit  

## Files

- `main.py` – main loop and program entry point  
- `settings.py` – simulation constants  
- `blocks.py` – block class  
- `physics.py` – collision logic and block creation  
- `ui.py` – rendering helpers  

## Notes

- Block behavior can be adjusted in `settings.py`  
- Collision handling is based on elastic collision equations