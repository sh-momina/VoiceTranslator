from llm.speech_cleanup import cleanup_text


while True:

    text = input("You: ")

    print()

    print(cleanup_text(text, "Me"))

    print()