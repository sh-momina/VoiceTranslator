# import soundcard as sc
# import soundfile as sf


# def capture_system_audio(seconds=3):

#     print("Capturing system audio...")

#     mic = sc.get_microphone(
#         "CABLE Input (VB-Audio Virtual Cable)",
#         include_loopback=True
#     )

#     data = mic.record(
#         samplerate=48000,
#         numframes=48000 * seconds
#     )

#     filename = "audio/input/system.wav"

#     sf.write(
#         filename,
#         data,
#         48000
#     )

#     print("Saved system.wav")

#     return filename




import soundcard as sc
import soundfile as sf
import numpy as np
import shared

SAMPLE_RATE = 48000
BLOCK_SIZE = 480          # 10 ms
MAX_SECONDS = 3


def capture_system_audio():

    print("Capturing system audio...")

    mic = sc.get_microphone(
        "CABLE Input (VB-Audio Virtual Cable)",
        include_loopback=True
    )

    recorded = []

    with mic.recorder(samplerate=SAMPLE_RATE) as recorder:

        blocks = int((SAMPLE_RATE * MAX_SECONDS) / BLOCK_SIZE)

        for _ in range(blocks):

            block = recorder.record(numframes=BLOCK_SIZE)

            # Ignore OUR translated audio
            if shared.playing_audio.is_set():
                continue

            recorded.append(block)

    if len(recorded) == 0:
        return None

    audio = np.concatenate(recorded, axis=0)

    filename = "audio/input/system.wav"

    sf.write(
        filename,
        audio,
        SAMPLE_RATE
    )

    print("Saved system.wav")

    return filename