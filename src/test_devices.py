import sounddevice as sd

for i in range(len(sd.query_devices())):

    try:

        print(f"\nTrying Device {i}")

        stream = sd.InputStream(
            device=i,
            channels=1,
            samplerate=16000,
            dtype="int16"
        )

        stream.start()

        stream.stop()

        stream.close()

        print("SUCCESS")

    except Exception as e:

        print("FAILED:", e)