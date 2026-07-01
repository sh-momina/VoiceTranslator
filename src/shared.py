# from queue import Queue
# from threading import Event

# audio_queue = Queue()

# speech_queue = Queue()

# running = Event()
# running.set()

# playing_audio = Event()

# my_language = None
# other_language = None



from queue import Queue
from threading import Event

audio_queue = Queue()
speech_queue = Queue()

running = Event()
running.set()

# True while translated audio is playing
playing_audio = Event()

my_language = None
other_language = None


last_input = ""
last_translation = ""

last_incoming = ""
last_incoming_translation = ""

status = "Ready"

latency = 0