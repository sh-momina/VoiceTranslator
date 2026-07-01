import os
from dotenv import load_dotenv
from groq import Groq

from llm.memory import memory


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


MODEL = "llama-3.1-8b-instant"


SYSTEM_PROMPT = """
You are a speech cleanup engine for a live voice translator.

Your job is ONLY to slightly clean speech recognition output.

STRICT RULES:

- Never answer the speaker.
- Never translate.
- Never summarize.
- Never rewrite.
- Never improve style.
- Never change meaning.
- Never add words unless absolutely necessary.
- Never remove conversational words like yes, yeah, okay, alright unless they are clearly duplicated by recognition errors.

Only perform these actions:

1. Fix obvious spelling mistakes.
2. Expand contractions like "u" -> "you".
3. Correct obvious speech-recognition mistakes.
4. Remove repeated words ONLY if they are clearly accidental recognition duplicates.
5. If the sentence already makes sense, return it unchanged.

Return ONLY the cleaned sentence.
"""


cache = {}


def cleanup_text(text, speaker):

    if not text:
        return text

    if text in cache:
        return cache[text]

    context = memory.get_context()

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },

        {
            "role": "user",
            "content":
f"""
Conversation:

{context}

Current Speaker:
{speaker}

Speech:

{text}
"""
        }

    ]

    response = client.chat.completions.create(

        model=MODEL,

        messages=messages,

        temperature=0,

        max_tokens=120

    )

    cleaned = response.choices[0].message.content.strip()

    memory.add(speaker, cleaned)

    cache[text] = cleaned

    return cleaned