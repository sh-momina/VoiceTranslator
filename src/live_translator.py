import time

from setup import setup_languages
from record import record_audio
from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech
from play_audio import play_audio


def main():

    print("\n======================================")
    print(" Live Voice Translator")
    print("======================================")

    my_language, other_language = setup_languages()

    print("\nTranslator Started")
    print("Press Ctrl + C to stop.\n")

    conversation = 1

    try:

        while True:

            print("\n--------------------------------------")
            print(f"Conversation #{conversation}")
            print("--------------------------------------")

            start = time.perf_counter()

            audio_file = record_audio()

            text = speech_to_text(
                audio_file,
                my_language["stt"]
            )

            if not text:
                continue

            translated = translate_text(
                text,
                my_language["translate"],
                other_language["translate"]
            )

            if not translated:
                continue

            voice = text_to_speech(
                translated,
                other_language["voice"]
            )

            play_audio(voice)

            end = time.perf_counter()

            print(f"\nCompleted in {end-start:.2f} sec")

            conversation += 1

    except KeyboardInterrupt:

        print("\n\nTranslator Stopped")


if __name__ == "__main__":

    main()