import speech_recognition as sr
import time


def speech_to_text(audio_file, language):

    print("\n==============================")
    print(" Speech To Text")
    print("==============================")

    recognizer = sr.Recognizer()

    start_time = time.perf_counter()

    with sr.AudioFile(audio_file) as source:

        audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(

            audio,

            language=language

        )

        end_time = time.perf_counter()

        print(f"Language Used : {language}")
        print(f"Recognized Text : {text}")
        print(f"Speech Recognition Time : {end_time-start_time:.2f} seconds")

        return text

    except sr.UnknownValueError:

        print("Could not understand audio.")

        return None

    except sr.RequestError:

        print("Internet Connection Error.")

        return None


if __name__ == "__main__":

    speech_to_text(

        "audio/input/recording.wav",

        "en-US"

    )