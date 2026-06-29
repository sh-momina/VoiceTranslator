import threading

from shared import audio_queue
from shared import text_queue

from speech_to_text import speech_to_text


class STTThread(threading.Thread):

    def __init__(self, my_language):

        super().__init__(daemon=True)

        self.my_language = my_language

    def run(self):

        print("STT Thread Started")

        while True:

            audio_file = audio_queue.get()

            text = speech_to_text(

                audio_file,

                self.my_language["stt"]

            )

            if text:

                text_queue.put(text)

                print("Text Added To Queue")