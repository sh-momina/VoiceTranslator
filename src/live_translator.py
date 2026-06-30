from setup import setup_languages
import time
import shared

from threads.listener import ListenerThread
from threads.processor import ProcessorThread
from threads.speaker import SpeakerThread

from incoming.incoming_listener import IncomingListener
from incoming.incoming_processor import IncomingProcessor
from incoming.incoming_speaker import IncomingSpeaker


def main():

    print("\n======================================")
    print(" Live Voice Translator")
    print("======================================")

    my_language, other_language = setup_languages()

    shared.my_language = my_language
    shared.other_language = other_language

    threads = [

        ListenerThread(),
        ProcessorThread(),
        SpeakerThread(),

        IncomingListener(),
        IncomingProcessor(),
        IncomingSpeaker()

    ]

    for thread in threads:
        thread.daemon = True
        thread.start()

    print("\nTranslator Started")
    print("Outgoing Translation : Running")
    print("Incoming Translation : Running")
    print("\nPress Ctrl + C to stop.\n")

    try:

        while shared.running.is_set():
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nStopping...")

    finally:

        shared.running.clear()

        print("Translator Stopped")


if __name__ == "__main__":
    main()