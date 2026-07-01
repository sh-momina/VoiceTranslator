from threading import Thread
from queue import Empty
import time

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

            pipeline_start = time.perf_counter()

            shared.status = "Recognizing incoming speech..."

            print("Incoming Processor received audio")

            # ---------------------------------
            # Speech To Text
            # ---------------------------------

            stt_start = time.perf_counter()

            text = speech_to_text(
                audio,
                shared.other_language["stt"]
            )

            stt_time = time.perf_counter() - stt_start

            print(f"Incoming STT Time : {stt_time:.2f} sec")
            print("Incoming Text:", text)

            shared.last_incoming = text if text else ""

            if not text:
                shared.status = "Waiting for speech..."
                continue

            # ---------------------------------
            # LLM Cleanup
            # ---------------------------------

            shared.status = "Cleaning incoming sentence..."

            cleanup_start = time.perf_counter()

            cleaned_text = cleanup_text(
                text,
                "Other"
            )

            cleanup_time = time.perf_counter() - cleanup_start

            print(f"Incoming Cleanup Time : {cleanup_time:.2f} sec")
            print("Incoming Cleaned:", cleaned_text)

            # ---------------------------------
            # Translation
            # ---------------------------------

            shared.status = "Translating incoming..."

            translate_start = time.perf_counter()

            translated = translate_text(
                cleaned_text,
                shared.other_language["translate"],
                shared.my_language["translate"]
            )

            translate_time = time.perf_counter() - translate_start

            print(f"Incoming Translate Time : {translate_time:.2f} sec")
            print("Incoming Translation:", translated)

            shared.last_incoming_translation = translated if translated else ""

            if not translated:
                shared.status = "Waiting for speech..."
                continue

            # ---------------------------------
            # Text To Speech
            # ---------------------------------

            shared.status = "Generating incoming voice..."

            tts_start = time.perf_counter()

            voice = text_to_speech(
                translated,
                shared.my_language["voice"]
            )

            tts_time = time.perf_counter() - tts_start

            print(f"Incoming TTS Time : {tts_time:.2f} sec")

            total_time = time.perf_counter() - pipeline_start

            print("\n==============================")
            print(" Incoming Pipeline Summary")
            print("==============================")
            print(f"STT       : {stt_time:.2f} sec")
            print(f"Cleanup   : {cleanup_time:.2f} sec")
            print(f"Translate : {translate_time:.2f} sec")
            print(f"TTS       : {tts_time:.2f} sec")
            print(f"TOTAL     : {total_time:.2f} sec")
            print("==============================\n")

            shared.status = "Playing incoming translation..."

            incoming_speech_queue.put(voice)

            shared.status = "Waiting for speech..."




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

# from llm.speech_cleanup import cleanup_text


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

#             # -------------------------
#             # Speech To Text
#             # -------------------------

#             text = speech_to_text(
#                 audio,
#                 shared.other_language["stt"]
#             )

#             print("Incoming Text:", text)

#             if not text:
#                 continue

#             # -------------------------
#             # LLM Cleanup
#             # -------------------------

#             cleaned_text = cleanup_text(
#                 text,
#                 "Other"
#             )

#             print("Incoming Cleaned:", cleaned_text)

#             # -------------------------
#             # Translation
#             # -------------------------

#             translated = translate_text(
#                 cleaned_text,
#                 shared.other_language["translate"],
#                 shared.my_language["translate"]
#             )

#             print("Incoming Translation:", translated)

#             if not translated:
#                 continue

#             # -------------------------
#             # Text To Speech
#             # -------------------------

#             voice = text_to_speech(
#                 translated,
#                 shared.my_language["voice"]
#             )

#             incoming_speech_queue.put(voice)