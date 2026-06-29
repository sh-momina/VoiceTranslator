import time

from setup import setup_languages
from record import record_audio
from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech
from play_audio import play_audio


print("\n========================================")
print(" Real-Time Continuous Translator ")
print("========================================")

# Language setup only once
my_language, other_language = setup_languages()

conversation_number = 1

while True:

    print("\n")
    print("=" * 50)
    print(f" Conversation #{conversation_number}")
    print("=" * 50)

    total_start = time.perf_counter()

    try:

        # Record
        audio_file = record_audio()

        # Speech To Text
        text = speech_to_text(
            audio_file,
            my_language["stt"]
        )

        if text is None:
            print("Speech Recognition Failed.")
            continue

        # Translate
        translated_text = translate_text(
            text,
            my_language["translate"],
            other_language["translate"]
        )

        if translated_text is None:
            print("Translation Failed.")
            continue

        # Text To Speech
        voice_file = text_to_speech(
            translated_text,
            other_language["voice"]
        )

        if voice_file is None:
            print("Voice Generation Failed.")
            continue

        # Play
        play_audio(voice_file)

        total_end = time.perf_counter()

        print("\nFinished.")
        print(f"Time : {total_end-total_start:.2f} sec")

        conversation_number += 1

    except KeyboardInterrupt:

        print("\nStopping Translator...")
        break

    except Exception as e:

        print(f"\nError : {e}")