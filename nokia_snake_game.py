# Main Modules
import customtkinter as ctk
import random

# Constance
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "brown"
FOOD_COLOR = "red"
BACKGROUND_COLOUR = "green"


# Main Game
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Only check for collision with itself, not with walls
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Stop movement if snake hits the wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return  # Do not move further, but do not end the game

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.configure(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        win.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction


def game_over():
    # Show a game over message and stop the game loop
    label.configure(text=f"Game Over! Final Score: {score}")
    canvas.delete("all")


win = ctk.CTk()
win.title("Snake Game")
win.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")

score = 0
direction = "down"

label = ctk.CTkLabel(win, text=f"Score:{score}", font=("consolas", 40))
label.pack()

canvas = ctk.CTkCanvas(win, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

win.bind("<Left>", lambda event: change_direction("left"))
win.bind("<Right>", lambda event: change_direction("right"))
win.bind("<Down>", lambda event: change_direction("down"))
win.bind("<Up>", lambda event: change_direction("up"))

snake = Snake()
food = Food()

next_turn(snake, food)

win.mainloop()
