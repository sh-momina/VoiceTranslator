from threading import Thread
from queue import Empty

from shared import speech_queue
from shared import running

from config import VB_CABLE_INPUT

from play_audio import play_audio


class SpeakerThread(Thread):

    def run(self):

        try:

            while running.is_set():

                print("Speaker waiting...")

                try:
                    voice = speech_queue.get(timeout=1)

                except Empty:
                    continue

                print("Playing through VB-CABLE...")

                play_audio(
                    voice,
                    output_device=VB_CABLE_INPUT
                )

        except Exception as e:

            print("SPEAKER THREAD ERROR:", e)

            import traceback
            traceback.print_exc()