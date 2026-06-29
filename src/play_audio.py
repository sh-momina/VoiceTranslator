import pygame
import time


def play_audio(audio_path):

    print("\n==============================")
    print(" Play Audio")
    print("==============================")

    start_time = time.perf_counter()

    pygame.mixer.init()

    pygame.mixer.music.load(audio_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    end_time = time.perf_counter()

    print(f"Played File : {audio_path}")
    print(f"Play Time   : {end_time-start_time:.2f} seconds")


if __name__ == "__main__":

    play_audio("audio/output/output.mp3")