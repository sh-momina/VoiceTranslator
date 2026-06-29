def setup_languages():

    print("\n========================================")
    print(" Voice Translator Setup")
    print("========================================")

    print("\nSelect Your Language")

    print("1. English")
    print("2. Urdu")

    my_choice = input("\nChoice : ")

    print("\nSelect Other Person Language")

    print("1. English")
    print("2. Urdu")

    other_choice = input("\nChoice : ")

    language_data = {

        "1": {
            "stt": "en-US",
            "translate": "en",
            "voice": "en-US-AriaNeural",
            "name": "English"
        },

        "2": {
            "stt": "ur-PK",
            "translate": "ur",
            "voice": "ur-PK-UzmaNeural",
            "name": "Urdu"
        }

    }

    my_language = language_data[my_choice]

    other_language = language_data[other_choice]

    print("\n==============================")

    print("Setup Completed")

    print("==============================")

    print(f"My Language      : {my_language['name']}")
    print(f"Other Language   : {other_language['name']}")

    return my_language, other_language


if __name__ == "__main__":

    setup_languages()