import sounddevice as sd
from scipy.io.wavfile import write
import time
import os
from config import INPUT_AUDIO
from config import SAMPLE_RATE
from config import CHANNELS
from config import RECORD_SECONDS


def record_audio():

    print("\n==============================")
    print(" Voice Recorder")
    print("==============================")

    input_folder = "audio/input"
    os.makedirs(input_folder, exist_ok=True)

    output_file = INPUT_AUDIO

    input("Press Enter and start speaking...")

    print("\nRecording...")

    start_time = time.perf_counter()

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    end_time = time.perf_counter()

    write(
        output_file,
        SAMPLE_RATE,
        audio
    )

    print("Recording Finished.")

    print(f"Saved at : {output_file}")

    print(f"Recording Time : {end_time - start_time:.2f} seconds")

    return output_file


if __name__ == "__main__":
    record_audio()