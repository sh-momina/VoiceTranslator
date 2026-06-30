from threading import Thread

from shared import speech_queue
from shared import running

from config import VB_CABLE_INPUT

from play_audio import play_audio


class SpeakerThread(Thread):

    def run(self):

        while running:

            print("Speaker waiting...")

            voice = speech_queue.get()

            print("Playing through VB-CABLE...")

            play_audio(
                voice,
                output_device=VB_CABLE_INPUT
            )