import pygame
import random

# Initialize all pygame modules
pygame.init()

# Fallback font in case pygame.font fails to initialize
font = None
try:
    if hasattr(pygame, 'font') and pygame.font.get_init():
        font = pygame.font.SysFont("Comic Sans MS", 20)
except (ImportError, NotImplementedError, AttributeError):
    font = None


def play_music():
    try:
        if hasattr(pygame, 'mixer') and pygame.mixer.get_init():
            music = "SpaceBot/bg_music.mp3"
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)
    except (ImportError, NotImplementedError, AttributeError) as e:
        print(f"Music module not available or error playing music: {e}")


WIDTH = 900
HEIGHT = 500
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
gold = (255, 215, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)  # New color for the robotic bird
silver = (192, 192, 192)  # New color for the robotic bird

win = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
pygame.display.set_caption("SpaceBot")

# variable library
player_x = 225
player_y = 225
y_change = 0
jump_height = 12
gravity = 0.9
obstacles = [400, 700, 1000, 1300, 1600]
generate_places = True
y_positions = []
speed = 5
game_over = False
score = 0
high_score = 0
stars = []


def draw_player(x_pos, y_pos, y_change):
    # Main body of the robotic bird
    player_body = pygame.draw.rect(win, silver, [x_pos, y_pos, 30, 30], 0, 10)

    # Futuristic beak (sharp triangle)
    pygame.draw.polygon(
        win,
        cyan,
        [[x_pos + 30, y_pos + 10], [x_pos + 40, y_pos + 15], [x_pos + 30, y_pos + 20]],
    )

    # Glowing eyes (cyan)
    pygame.draw.circle(win, cyan, [x_pos + 10, y_pos + 12], 3)
    pygame.draw.circle(win, cyan, [x_pos + 20, y_pos + 12], 3)

    # Angular fins/wings
    pygame.draw.polygon(
        win, silver, [[x_pos, y_pos + 5], [x_pos - 10, y_pos + 15], [x_pos, y_pos + 25]]
    )

    # Thruster at the back
    thruster = pygame.draw.rect(win, gray, [x_pos - 5, y_pos + 25, 30, 15], 0, 2)

    # Flames from the thruster when jumping
    if y_change < 0:
        flame_red1 = pygame.draw.rect(win, cyan, [x_pos - 2, y_pos + 35, 12, 15], 0, 2)
        flame_yellow1 = pygame.draw.rect(win, green, [x_pos, y_pos + 36, 8, 12], 0, 2)

    return player_body


def draw_obstacles(obst, y_pos, char):
    global game_over

    for i in range(len(obst)):
        y_coord = y_pos[i]
        top_rect = pygame.draw.rect(win, gray, [obst[i], 0, 30, y_coord])
        top_rect_top = pygame.draw.rect(
            win, gray, [obst[i] - 3, y_coord - 20, 36, 20], 0, 5
        )
        bottom_rect = pygame.draw.rect(
            win, gray, [obst[i], y_coord + 200, 30, HEIGHT - (y_coord + 70)]
        )
        bottom_rect_top = pygame.draw.rect(
            win, gray, [obst[i] - 3, y_coord + 200, 36, 20], 0, 5
        )
        if top_rect.colliderect(char) or bottom_rect.colliderect(char):
            game_over = True


def draw_stars(obj):
    global total

    for i in range(total - 1):
        pygame.draw.rect(win, white, [obj[i][0], obj[i][1], 3, 3], 0, 2)
        obj[i][0] -= 0.5
        if obj[i][0] < -3:
            obj[i][0] = WIDTH - 3
            obj[i][1] = random.randint(0, HEIGHT)

    return obj


play_music()

running = True
while running:
    timer.tick(fps)
    win.fill(black)

    if generate_places:
        for i in range(len(obstacles)):
            y_positions.append(random.randint(0, 300))

        total = 100
        for i in range(total):
            x_pos = random.randint(0, WIDTH)
            y_pos = random.randint(0, HEIGHT)
            stars.append([x_pos, y_pos])

        generate_places = False

    stars = draw_stars(stars)
    player = draw_player(player_x, player_y, y_change)
    draw_obstacles(obstacles, y_positions, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_SPACE, pygame.K_w) and not game_over:
                if player_y < 0:
                    player_y = 0
                else:
                    y_change = -jump_height
            if (event.key == pygame.K_SPACE) and game_over:
                player_y = 225
                player_x = 225
                y_change = 0
                generate_places = True
                obstacles = [400, 700, 1000, 1300, 1600]
                generate_places = True
                y_positions = []
                score = 0
                game_over = False

    if player_y + y_change < HEIGHT - 30:
        player_y += y_change
        y_change += gravity
        if player_y < 0:
            player_y = 0
            y_change = 0
    else:
        player_y = HEIGHT - 30

    for i in range(len(obstacles)):
        if not game_over:
            obstacles[i] -= speed
            if obstacles[i] < -30:
                obstacles.remove(obstacles[i])
                y_positions.remove(y_positions[i])
                obstacles.append(
                    random.randint(obstacles[-1] + 200, obstacles[-1] + 320)
                )
                y_positions.append(random.randint(0, 300))
                score += 1

    if score > high_score:
        high_score = score

    if font:
        if game_over:
            game_over_text = font.render("Press Space to Restart!!", True, white)
            win.blit(game_over_text, (325, 225))

        score_text = font.render(f"Score:{score}", True, white)
        win.blit(score_text, (10, 450))
        highscore_text = font.render(f"High Score:{high_score}", True, white)
        win.blit(highscore_text, (10, 470))

    pygame.display.flip()

pygame.quit()
