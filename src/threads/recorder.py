import threading

from record import record_audio
from shared import audio_queue


class RecorderThread(threading.Thread):

    def __init__(self):

        super().__init__(daemon=True)

    def run(self):

        print("Recorder Thread Started")

        while True:

            audio_file = record_audio()

            if audio_file is not None:

                audio_queue.put(audio_file)

                print("Audio Added To Queue")