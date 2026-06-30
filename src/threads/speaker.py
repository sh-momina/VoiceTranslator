from threading import Thread

import shared

from shared import speech_queue

from play_audio import play_audio


class SpeakerThread(Thread):

    def run(self):

        while shared.running:

            print("Speaker waiting...")

            voice = speech_queue.get()

            print("Speaker playing...")

            play_audio(voice)