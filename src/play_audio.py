import pygame
import time
import os


def play_audio(audio_file):

    print("\n==============================")
    print(" Play Audio")
    print("==============================")

    pygame.mixer.init()

    pygame.mixer.music.load(audio_file)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        time.sleep(0.1)

    pygame.mixer.music.unload()

    pygame.mixer.quit()

    try:
        os.remove(audio_file)
    except:
        pass

    print("Finished")