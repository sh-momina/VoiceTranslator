# Audio Files

INPUT_AUDIO = "audio/input/recording.wav"

OUTPUT_AUDIO = "audio/output/output.mp3"


# Recording

RECORD_SECONDS = 7
SAMPLE_RATE = 16000
CHANNELS = 1


# Languages
# These values are changed by setup.py

MY_LANGUAGE = ""
OTHER_LANGUAGE = ""

THRESHOLD = 0.003

CHANNELS = 1

# ==============================
# Voice Activity Detection (VAD)
# ==============================



CHUNK_DURATION_MS = 30      # WebRTC supports 10, 20, or 30 ms

VAD_MODE = 2                # 0=least aggressive, 3=most aggressive

MAX_SILENCE_MS = 800        # Stop after 0.8 sec silence

PRE_SPEECH_MS = 300         # Keep a little audio before speech starts

# Audio Files
INPUT_AUDIO = "audio/input/recording.wav"
OUTPUT_AUDIO = "audio/output/output.mp3"

# Audio Settings
SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_DURATION = 0.03      # 30 ms
SILENCE_DURATION = 1.0      # seconds
THRESHOLD = 0.01            # only used as backup