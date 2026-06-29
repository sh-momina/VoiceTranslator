import queue
from collections import deque

import sounddevice as sd
import webrtcvad

from config import (
    SAMPLE_RATE,
    CHANNELS,
    CHUNK_DURATION_MS,
    VAD_MODE,
    PRE_SPEECH_MS,
)


def vad_record():

    print("\n==============================")
    print(" WebRTC Voice Recorder")
    print("==============================")

    print("Waiting for speech...\n")

    vad = webrtcvad.Vad(VAD_MODE)

    audio_queue = queue.Queue()

    # Recording State
    frames = []
    recording = False
    silence_ms = 0

    # Buffer to keep audio before speech starts
    pre_buffer = deque(
        maxlen=PRE_SPEECH_MS // CHUNK_DURATION_MS
    )

    frame_size = int(
        SAMPLE_RATE * CHUNK_DURATION_MS / 1000
    )

    def callback(indata, frames, time, status):

        audio_queue.put(indata.copy())

    with sd.InputStream(

        samplerate=SAMPLE_RATE,

        channels=CHANNELS,

        dtype="int16",

        blocksize=frame_size,

        callback=callback

    ):

        while True:

            chunk = audio_queue.get()

            # Always keep recent audio in memory
            pre_buffer.append(chunk)

            audio_bytes = chunk.tobytes()

            speech = vad.is_speech(
                audio_bytes,
                SAMPLE_RATE
            )

            if speech:

                if not recording:

                    print("\nSpeech Started")

                    recording = True

                    # Copy buffered audio collected before speech
                    frames.extend(pre_buffer)

                silence_ms = 0

                frames.append(chunk)

            else:

                if recording:

                    print("Silence")

                else:

                    print("Waiting...")

    return frames


if __name__ == "__main__":

    vad_record()