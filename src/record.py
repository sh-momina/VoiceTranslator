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
    BLOCK_DURATION,
    SILENCE_DURATION,
)

audio_queue = queue.Queue()


def audio_callback(indata, frames, time_info, status):

    if status:
        print(status)

    audio_queue.put(indata.copy())


def record_audio():

    print("\n==============================")
    print(" Voice Recorder")
    print("==============================")

    os.makedirs("audio/input", exist_ok=True)

    print("Waiting for speech...\n")

    frames = []

    recording = False

    silence_blocks = 0

    max_silence_blocks = int(
        SILENCE_DURATION / BLOCK_DURATION
    )

    start_time = None

    with sd.InputStream(

        samplerate=SAMPLE_RATE,

        channels=CHANNELS,

        dtype="float32",

        blocksize=int(SAMPLE_RATE * BLOCK_DURATION),

        callback=audio_callback

    ):

        while True:

            chunk = audio_queue.get()

            volume = np.sqrt(np.mean(chunk ** 2))

            print(f"Volume : {volume:.5f}")

            if not recording:

                if volume > 0.01:

                    print("\nSpeech Detected\n")

                    recording = True

                    start_time = time.perf_counter()

                    frames.append(chunk)

            else:

                frames.append(chunk)

                if volume > 0.01:

                    silence_blocks = 0

                else:

                    silence_blocks += 1

                    if silence_blocks >= max_silence_blocks:

                        break

    audio = np.concatenate(frames)

    write(
        INPUT_AUDIO,
        SAMPLE_RATE,
        (audio * 32767).astype(np.int16)
    )

    end_time = time.perf_counter()

    print("Recording Finished")
    print(f"Saved : {INPUT_AUDIO}")
    print(f"Duration : {end_time-start_time:.2f} sec")

    return INPUT_AUDIO


if __name__ == "__main__":

    record_audio()