from collections import deque


class ConversationMemory:

    def __init__(self, max_messages=20):
        self.history = deque(maxlen=max_messages)

    def add(self, speaker, text):

        if text:
            self.history.append({
                "speaker": speaker,
                "text": text
            })

    def get_context(self):

        if not self.history:
            return ""

        return "\n".join(
            f'{item["speaker"]}: {item["text"]}'
            for item in self.history
        )


memory = ConversationMemory()