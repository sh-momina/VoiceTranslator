from threading import Thread
from queue import Empty
from incoming.incoming_shared import incoming_speech_queue
import time
from shared import running

from play_audio import play_audio

from config import SPEAKER_DEVICE


class IncomingSpeaker(Thread):

    def run(self):

        print("Incoming Speaker Started")

        while running.is_set():

            try:
                voice = incoming_speech_queue.get(timeout=1)
            except Empty:
                continue

            print("\nPlaying translated incoming audio...")
        
            play_audio(
                voice,
                output_device=SPEAKER_DEVICE
            )