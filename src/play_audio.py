import os
import sounddevice as sd
import soundfile as sf
import shared


def play_audio(audio_file, output_device=None):

    print("\n==============================")
    print(" Play Audio")
    print("==============================")

    if not os.path.exists(audio_file):
        print("Audio file not found.")
        return

    data, samplerate = sf.read(audio_file, dtype="float32")

    if output_device is None:
        print("Playing on default speaker...")
    else:
        print(f"Playing on device {output_device}...")

    # Tell IncomingListener not to record
    shared.playing_audio.set()

    sd.play(
        data,
        samplerate,
        device=output_device
    )

    sd.wait()

    # Allow recording again
    shared.playing_audio.clear()

    print("Finished")