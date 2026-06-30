import sounddevice as sd
import soundfile as sf
import os


def play_audio(audio_file, output_device=None):

    print("\n==============================")
    print(" Play Audio")
    print("==============================")

    if not os.path.exists(audio_file):
        print("Audio file not found.")
        return

    data, samplerate = sf.read(audio_file, dtype="float32")

    sd.play(
        data,
        samplerate,
        device=output_device
    )

    sd.wait()

    print("Finished")