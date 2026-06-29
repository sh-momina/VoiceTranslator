from deep_translator import GoogleTranslator
import time


def translate_text(text, source_language, target_language):

    print("\n==============================")
    print(" Translation")
    print("==============================")

    start_time = time.perf_counter()

    translated = GoogleTranslator(
        source=source_language,
        target=target_language
    ).translate(text)

    end_time = time.perf_counter()

    print(f"Source Language : {source_language}")
    print(f"Target Language : {target_language}")
    print(f"Original Text   : {text}")
    print(f"Translated Text : {translated}")
    print(f"Translation Time: {end_time-start_time:.2f} seconds")

    return translated


if __name__ == "__main__":

    text = input("Enter text : ")

    translate_text(
        text,
        "en",
        "ur"
    )