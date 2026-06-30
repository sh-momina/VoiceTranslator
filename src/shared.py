from queue import Queue
from threading import Event

audio_queue = Queue()

speech_queue = Queue()

running = Event()
running.set()

playing_audio = Event()

my_language = None
other_language = None