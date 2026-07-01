from threading import Thread
from queue import Empty
import time

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

            shared.status = "Waiting for speech..."
            print("Processor waiting...")

            try:
                audio = audio_queue.get(timeout=1)

            except Empty:
                continue

            pipeline_start = time.perf_counter()

            shared.status = "Speech Recognized"

            print("Processor received audio")

            # ---------------------------------
            # Speech To Text
            # ---------------------------------

            stt_start = time.perf_counter()

            text = speech_to_text(
                audio,
                shared.my_language["stt"]
            )

            stt_time = time.perf_counter() - stt_start

            print(f"STT Time : {stt_time:.2f} sec")
            print("Recognized:", text)

            shared.last_input = text if text else ""

            if not text:
                shared.status = "Waiting for speech..."
                continue

            # ---------------------------------
            # LLM Cleanup
            # ---------------------------------

            shared.status = "Cleaning sentence..."

            cleanup_start = time.perf_counter()

            cleaned_text = cleanup_text(
                text,
                "Me"
            )

            cleanup_time = time.perf_counter() - cleanup_start

            print(f"Cleanup Time : {cleanup_time:.2f} sec")
            print("Cleaned:", cleaned_text)

            # ---------------------------------
            # Translation
            # ---------------------------------

            shared.status = "Translating..."

            translate_start = time.perf_counter()

            translated = translate_text(
                cleaned_text,
                shared.my_language["translate"],
                shared.other_language["translate"]
            )

            translate_time = time.perf_counter() - translate_start

            print(f"Translate Function Time : {translate_time:.2f} sec")
            print("Translated:", translated)

            shared.last_translation = translated if translated else ""

            if not translated:
                shared.status = "Waiting for speech..."
                continue

            # ---------------------------------
            # Text To Speech
            # ---------------------------------

            shared.status = "Generating voice..."

            tts_start = time.perf_counter()

            voice = text_to_speech(
                translated,
                shared.other_language["voice"]
            )

            tts_time = time.perf_counter() - tts_start

            print(f"TTS Time : {tts_time:.2f} sec")

            total_time = time.perf_counter() - pipeline_start

            shared.latency = round(total_time, 2)

            print("\n==============================")
            print(" Pipeline Summary")
            print("==============================")
            print(f"STT       : {stt_time:.2f} sec")
            print(f"Cleanup   : {cleanup_time:.2f} sec")
            print(f"Translate : {translate_time:.2f} sec")
            print(f"TTS       : {tts_time:.2f} sec")
            print(f"TOTAL     : {total_time:.2f} sec")
            print("==============================\n")

            shared.status = "Speaking..."

            speech_queue.put(voice)

            shared.status = "Waiting for speech..."




# from threading import Thread
# from queue import Empty

# import shared

# from shared import audio_queue
# from shared import speech_queue

# from speech_to_text import speech_to_text
# from translate import translate_text
# from text_to_speech import text_to_speech

# from llm.speech_cleanup import cleanup_text


# class ProcessorThread(Thread):

#     def run(self):

#         while shared.running.is_set():

#             print("Processor waiting...")

#             try:
#                 audio = audio_queue.get(timeout=1)

#             except Empty:
#                 continue

#             print("Processor received audio")

#             # -------------------------
#             # Speech To Text
#             # -------------------------

#             text = speech_to_text(
#                 audio,
#                 shared.my_language["stt"]
#             )

#             print("Recognized:", text)
#             shared.last_input = text

#             if not text:
#                 continue

#             # -------------------------
#             # LLM Cleanup
#             # -------------------------

#             cleaned_text = cleanup_text(
#                 text,
#                 "Me"
#             )

#             print("Cleaned:", cleaned_text)

#             # -------------------------
#             # Translation
#             # -------------------------

#             translated = translate_text(
#                 cleaned_text,
#                 shared.my_language["translate"],
#                 shared.other_language["translate"]
#             )

#             print("Translated:", translated)
#             shared.last_translation = translated

#             if not translated:
#                 continue

#             # -------------------------
#             # Text To Speech
#             # -------------------------

#             voice = text_to_speech(
#                 translated,
#                 shared.other_language["voice"]
#             )

#             speech_queue.put(voice)


