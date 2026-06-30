from threading import Thread

import shared

from shared import audio_queue
from shared import speech_queue

from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech


class ProcessorThread(Thread):

    def run(self):

        while shared.running:

            print("Processor waiting...")

            audio = audio_queue.get()

            print("Processor received audio")

            text = speech_to_text(
                audio,
                shared.my_language["stt"]
            )

            print("Recognized:", text)

            if not text:
                continue

            translated = translate_text(
                text,
                shared.my_language["translate"],
                shared.other_language["translate"]
            )

            print("Translated:", translated)

            if not translated:
                continue

            voice = text_to_speech(
                translated,
                shared.other_language["voice"]
            )

            speech_queue.put(voice)