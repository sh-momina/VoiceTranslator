import soundcard as sc
import soundfile as sf


def capture_system_audio(seconds=3):

    print("Capturing system audio...")

    mic = sc.get_microphone(
        "CABLE Input (VB-Audio Virtual Cable)",
        include_loopback=True
    )

    data = mic.record(
        samplerate=48000,
        numframes=48000 * seconds
    )

    filename = "audio/input/system.wav"

    sf.write(
        filename,
        data,
        48000
    )

    print("Saved system.wav")

    return filename