# from threading import Thread

# import shared
# from queue import Empty
# from shared import audio_queue
# from shared import speech_queue

# from speech_to_text import speech_to_text
# from translate import translate_text
# from text_to_speech import text_to_speech


# class ProcessorThread(Thread):

#     def run(self):

#         while shared.running.is_set(): 

#             print("Processor waiting...")

#             try:
#                 audio = audio_queue.get(timeout=1)
#             except Empty:
#                 continue

#             print("Processor received audio")

#             text = speech_to_text(
#                 audio,
#                 shared.my_language["stt"]
#             )

#             print("Recognized:", text)

#             if not text:
#                 continue

#             translated = translate_text(
#                 text,
#                 shared.my_language["translate"],
#                 shared.other_language["translate"]
#             )

#             print("Translated:", translated)

#             if not translated:
#                 continue

#             voice = text_to_speech(
#                 translated,
#                 shared.other_language["voice"]
#             )

#             speech_queue.put(voice)






from threading import Thread
from queue import Empty

import shared

from shared import audio_queue
from shared import speech_queue

from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech

from llm.speech_cleanup import cleanup_text


class ProcessorThread(Thread):

    def run(self):

        while shared.running.is_set():

            print("Processor waiting...")

            try:
                audio = audio_queue.get(timeout=1)

            except Empty:
                continue

            print("Processor received audio")

            # -------------------------
            # Speech To Text
            # -------------------------

            text = speech_to_text(
                audio,
                shared.my_language["stt"]
            )

            print("Recognized:", text)

            if not text:
                continue

            # -------------------------
            # LLM Cleanup
            # -------------------------

            cleaned_text = cleanup_text(
                text,
                "Me"
            )

            print("Cleaned:", cleaned_text)

            # -------------------------
            # Translation
            # -------------------------

            translated = translate_text(
                cleaned_text,
                shared.my_language["translate"],
                shared.other_language["translate"]
            )

            print("Translated:", translated)

            if not translated:
                continue

            # -------------------------
            # Text To Speech
            # -------------------------

            voice = text_to_speech(
                translated,
                shared.other_language["voice"]
            )

            speech_queue.put(voice)


