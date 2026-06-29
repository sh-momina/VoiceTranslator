from threading import Thread

from shared import audio_queue
from record import record_audio


class RecorderThread(Thread):

    def __init__(self):
        super().__init__(daemon=True)

    def run(self):

        while True:

            audio = record_audio()

            audio_queue.put(audio)