import time

from setup import setup_languages

from threads.recorder_thread import RecorderThread
from threads.processor_thread import ProcessorThread


print("\n======================================")
print(" Live Translator (Threaded)")
print("======================================")

my_language, other_language = setup_languages()

recorder = RecorderThread()

processor = ProcessorThread(
    my_language,
    other_language
)

recorder.start()
processor.start()

print("\nTranslator Running...")
print("Press Ctrl+C to stop.")

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    print("\nTranslator Stopped")