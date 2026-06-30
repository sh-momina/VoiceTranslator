import asyncio
import uuid
import os
import edge_tts

OUTPUT_FOLDER = "audio/output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


async def generate_voice(text, voice, filename):

    communicate = edge_tts.Communicate(text, voice)

    await communicate.save(filename)


def text_to_speech(text, voice):

    filename = os.path.join(
        OUTPUT_FOLDER,
        f"{uuid.uuid4().hex}.mp3"
    )

    asyncio.run(
        generate_voice(
            text,
            voice,
            filename
        )
    )

    print("\n==============================")
    print(" Text To Speech")
    print("==============================")
    print("Voice :", voice)
    print("Saved :", filename)

    return filename