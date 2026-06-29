import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
CHANNELS = 1
DEVICE = 17          # Stereo Mix

print("Play a YouTube video or music...")
input("Press Enter to start recording...")

audio = sd.rec(
    SAMPLE_RATE * 5,
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="int16",
    device=DEVICE
)

sd.wait()

write(
    "audio/input/stereo_test.wav",
    SAMPLE_RATE,
    audio
)

print("Saved!")