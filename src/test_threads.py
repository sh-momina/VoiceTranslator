import time

from setup import setup_languages

from threads.recorder import RecorderThread
from threads.stt import STTThread


print("\n==============================")
print(" Thread Test")
print("==============================")

my_language, other_language = setup_languages()

recorder = RecorderThread()

stt = STTThread(my_language)

recorder.start()

stt.start()

print("\nThreads Running...\n")

while True:

    time.sleep(1)