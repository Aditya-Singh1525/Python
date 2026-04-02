import time
import pygame

pygame.init()
pygame.mixer.init()

ask = input("Enter how long should the timer run: ")
if ask.isdigit():
    ask = int(ask)
else:
    raise Exception("Invalid Input!")

print("")

for i in range(ask, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("\nCountdown is over!!")


def play_sound():
    try:
        mp3_file_path = (
            "Timer/timer_end.mp3"  #! <--- **CHANGE THIS TO YOUR REAL MP3 FILE PATH**
        )

        pygame.mixer.music.load(mp3_file_path)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(3)  # Plays 3 times

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)

        print("\nSound playback finished.")

    except pygame.error as error:
        print(f"Error playing sound: {error}")
    finally:
        pass


play_sound()
