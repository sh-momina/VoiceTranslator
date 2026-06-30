from threading import Thread

from shared import audio_queue
from shared import running

from record_stream import record_audio


class ListenerThread(Thread):

    def run(self):

        while running:

            audio = record_audio()

            if audio:

                print("Listener -> Audio captured")

                audio_queue.put(audio)