from threading import Thread
import traceback
import time
import shared
import time
from incoming.incoming_audio import capture_system_audio
from incoming.incoming_shared import incoming_audio_queue

class IncomingListener(Thread):

    def run(self):

        print("\nIncoming Listener Started")

        while shared.running.is_set():

            try:

                # Don't record while OUR translated audio is playing
                while shared.playing_audio.is_set() and shared.running.is_set():
                    time.sleep(0.1)
                    

                # audio = capture_system_audio(seconds=3)
                # audio = capture_system_audio(seconds=1)
                audio = capture_system_audio()


                if audio is None:
                    continue

                print("Incoming Audio Captured")

                incoming_audio_queue.put(audio)

            except Exception as e:

                print("\nINCOMING LISTENER ERROR")
                print(e)
                traceback.print_exc()