from text_to_speech import text_to_speech
from play_audio import play_audio

voice = text_to_speech(
    "Hello this is a speaker test",
    "en-US-AriaNeural"
)

play_audio(
    voice,
    output_device=16
)