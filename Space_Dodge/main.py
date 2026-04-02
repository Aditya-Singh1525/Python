import pygame
import time
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()


def play_music():
    music = "Space_Dodge/bg_music.mp3"
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)


def play_music_lost():
    music = "Space_Dodge/lose.mp3"
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)


width, height = 1200, 720  # ! Set this according to your display size.

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Dodge")

bg = pygame.transform.scale(pygame.image.load("Space_Dodge/bg.jpeg"), (width, height))

player_width = 40
player_height = 60
player_vel = 12

star_width = 10
star_height = 20
star_vel = 9

font = pygame.font.SysFont("Comic Sans MS", 30)


def draw(player, elapsed_time, stars):
    win.blit(bg, (0, 0))

    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    win.blit(time_text, (10, 10))

    pygame.draw.rect(win, "purple", player)

    for star in stars:
        pygame.draw.rect(win, "white", star)

    pygame.display.update()


def main():
    play_music()

    run = True

    player = pygame.Rect(200, height - player_height, player_width, player_height)
    clock = pygame.time.Clock()
    star_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []

    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - star_time

        if star_count > star_add_increment:
            for i in range(3):
                i = i
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (player.x - player_vel >= 0):
            player.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (
            player.x + player_vel + player.width <= width
        ):
            player.x += player_vel

        for star in stars[:]:
            star.y += star_vel
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            pygame.mixer.music.stop()
            play_music_lost()
            lost_text = font.render("You, Lose!", 1, "white")
            win.blit(
                lost_text,
                (
                    width / 2 - lost_text.get_width() / 2,
                    height / 2 - lost_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(5600)
            break  # Exit the game loop immediately after showing the message

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
