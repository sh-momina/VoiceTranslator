import time

from setup import setup_languages
from record import record_audio
from speech_to_text import speech_to_text
from translate import translate_text
from text_to_speech import text_to_speech
from play_audio import play_audio


print("\n========================================")
print(" Real-Time Voice Translator Prototype ")
print("========================================")

total_start = time.perf_counter()

# Select Languages
my_language, other_language = setup_languages()

# Record Voice
audio_file = record_audio()

# Speech To Text
text = speech_to_text(
    audio_file,
     my_language["stt"]
)

if text is None:

    print("Speech Recognition Failed.")
    exit()

# Translate
translated_text = translate_text(
    text,
    my_language["translate"],
    other_language["translate"]
)

if translated_text is None:

    print("Translation Failed.")
    exit()

# Text To Speech
voice_file = text_to_speech(
    translated_text,
    other_language["voice"]
)

if voice_file is None:

    print("Voice Generation Failed.")
    exit()

# Play Audio
play_audio(voice_file)

total_end = time.perf_counter()

print("\n========================================")
print(" Pipeline Finished Successfully ")
print("========================================")

print(f"Total Time : {total_end-total_start:.2f} seconds")