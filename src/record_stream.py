import os
import time
import queue

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

from config import (
    INPUT_AUDIO,
    SAMPLE_RATE,
    CHANNELS,
)

CHUNK_DURATION = 0.2
THRESHOLD = 0.008
SILENCE_DURATION = 1.0


class StreamRecorder:

    def __init__(self):

        self.q = queue.Queue()

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            blocksize=int(CHUNK_DURATION * SAMPLE_RATE),
            callback=self.audio_callback,
        )

        self.stream.start()

        print("\nMicrophone Stream Started\n")

    def audio_callback(self, indata, frames, time_info, status):

        if status:
            print(status)

        self.q.put(indata.copy())

    def record_audio(self):

        print("Waiting for speech...\n")

        recording = False

        silence = 0

        frames = []

        start = None

        while True:

            chunk = self.q.get()

            volume = np.abs(chunk).mean()

            if not recording:

                if volume > THRESHOLD:

                    print("Speech Detected")

                    recording = True

                    start = time.perf_counter()

                    frames.append(chunk)

            else:

                frames.append(chunk)

                if volume > THRESHOLD:

                    silence = 0

                else:

                    silence += CHUNK_DURATION

                    if silence >= SILENCE_DURATION:

                        break

        audio = np.concatenate(frames)

        os.makedirs("audio/input", exist_ok=True)

        write(
            INPUT_AUDIO,
            SAMPLE_RATE,
            (audio * 32767).astype(np.int16),
        )

        end = time.perf_counter()

        print(f"Saved : {INPUT_AUDIO}")
        print(f"Duration : {end-start:.2f} sec")

        return INPUT_AUDIO


recorder = StreamRecorder()


def record_audio():

    return recorder.record_audio()