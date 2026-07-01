# from threading import Thread
# from queue import Empty
# import shared

# from incoming.incoming_shared import (
#     incoming_audio_queue,
#     incoming_speech_queue,
# )

# from speech_to_text import speech_to_text
# from translate import translate_text
# from text_to_speech import text_to_speech


# class IncomingProcessor(Thread):

#     def run(self):

#         print("Incoming Processor Started")

#         while shared.running.is_set():

#             print("Incoming Processor waiting...")

#             try:
#                 audio = incoming_audio_queue.get(timeout=1)
#             except Empty:
#                 continue

#             print("Incoming Processor received audio")

#             text = speech_to_text(
#                 audio,
#                 shared.other_language["stt"]
#             )

#             print("Incoming Text:", text)

#             if not text:
#                 continue

#             translated = translate_text(
#                 text,
#                 shared.other_language["translate"],
#                 shared.my_language["translate"]
#             )

#             print("Incoming Translation:", translated)

#             if not translated:
#                 continue

#             voice = text_to_speech(
#                 translated,
#                 shared.my_language["voice"]
#             )

#             incoming_speech_queue.put(voice)





from threading import Thread
from queue import Empty

import shared

from incoming.incoming_shared import (
    incoming_audio_queue,
    incoming_speech_queue,
)

from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech

from llm.speech_cleanup import cleanup_text


class IncomingProcessor(Thread):

    def run(self):

        print("Incoming Processor Started")

        while shared.running.is_set():

            print("Incoming Processor waiting...")

            try:
                audio = incoming_audio_queue.get(timeout=1)

            except Empty:
                continue

            print("Incoming Processor received audio")

            # -------------------------
            # Speech To Text
            # -------------------------

            text = speech_to_text(
                audio,
                shared.other_language["stt"]
            )

            print("Incoming Text:", text)

            if not text:
                continue

            # -------------------------
            # LLM Cleanup
            # -------------------------

            cleaned_text = cleanup_text(
                text,
                "Other"
            )

            print("Incoming Cleaned:", cleaned_text)

            # -------------------------
            # Translation
            # -------------------------

            translated = translate_text(
                cleaned_text,
                shared.other_language["translate"],
                shared.my_language["translate"]
            )

            print("Incoming Translation:", translated)

            if not translated:
                continue

            # -------------------------
            # Text To Speech
            # -------------------------

            voice = text_to_speech(
                translated,
                shared.my_language["voice"]
            )

            incoming_speech_queue.put(voice)