import asyncio
import time
import edge_tts

OUTPUT_FILE = "audio/output/output.mp3"


async def generate_voice(text, voice):

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(OUTPUT_FILE)


def text_to_speech(text, voice):

    print("\n==============================")
    print(" Text To Speech")
    print("==============================")

    start_time = time.perf_counter()

    asyncio.run(
        generate_voice(
            text,
            voice
        )
    )

    end_time = time.perf_counter()

    print(f"Voice Used      : {voice}")
    print(f"Saved File      : {OUTPUT_FILE}")
    print(f"Generation Time : {end_time-start_time:.2f} seconds")

    return OUTPUT_FILE


if __name__ == "__main__":

    text = input("Enter text : ")

    text_to_speech(
        text,
        "en-US-AriaNeural"
    )