from threading import Thread

from shared import audio_queue

from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech
from play_audio import play_audio


class ProcessorThread(Thread):

    def __init__(self, my_language, other_language):
        super().__init__(daemon=True)

        self.my_language = my_language
        self.other_language = other_language

    def run(self):

        while True:

            audio = audio_queue.get()

            text = speech_to_text(
                audio,
                self.my_language["stt"]
            )

            if text is None:
                continue

            translated = translate_text(
                text,
                self.my_language["translate"],
                self.other_language["translate"]
            )

            if translated is None:
                continue

            voice = text_to_speech(
                translated,
                self.other_language["voice"]
            )

            play_audio(voice)