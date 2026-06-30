import shared

from setup import setup_languages

from threads.listener import ListenerThread
from threads.processor import ProcessorThread
from threads.speaker import SpeakerThread


def main():

    print("\n======================================")
    print(" Live Voice Translator")
    print("======================================")

    my_lang, other_lang = setup_languages()

    shared.my_language = my_lang
    shared.other_language = other_lang

    listener = ListenerThread()
    processor = ProcessorThread()
    speaker = SpeakerThread()

    listener.daemon = True
    processor.daemon = True
    speaker.daemon = True

    listener.start()
    processor.start()
    speaker.start()

    print("\nTranslator Started")
    print("Press Ctrl + C to stop.\n")

    try:

        while True:
            pass

    except KeyboardInterrupt:

        shared.running = False

        print("\nTranslator Stopped")


if __name__ == "__main__":
    main()