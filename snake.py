import random
import js

# Game settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
SPEED = 15

direction = "RIGHT"
snake = [[WIDTH // 2, HEIGHT // 2]]
food = [random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE]

def update():
    global direction, snake, food
    head = snake[-1][:]

    if direction == "LEFT":
        head[0] -= BLOCK_SIZE
    elif direction == "RIGHT":
        head[0] += BLOCK_SIZE
    elif direction == "UP":
        head[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        head[1] += BLOCK_SIZE

    # Wrap-around logic
    head[0] %= WIDTH
    head[1] %= HEIGHT

    snake.append(head)
    if head == food:
        food = [random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE]
    else:
        snake.pop(0)

    # Send updated game state to JavaScript
    js.update_canvas(to_js(snake), to_js(food))

def set_direction(new_direction):
    global direction
    if (direction, new_direction) not in [("LEFT", "RIGHT"), ("RIGHT", "LEFT"), ("UP", "DOWN"), ("DOWN", "UP")]:
        direction = new_direction

# Expose functions to JavaScript
from pyodide.ffi import to_js
js.set("update", update)
js.set("set_direction", set_direction)
