import os

from litellm import completion
from core.prompt import system_prompt, user_prompt


class LLM:
    def __init__(self):
        from dotenv import load_dotenv
        load_dotenv()

        self.messages = [
            {"content": system_prompt, "role": "system"}
        ]
        self.model = os.getenv("GPT_MODEL_4", "")

    def completion(self, question):
        self.messages.append(
            {"content": user_prompt.format(question=question), "role": "user"}
        )
        return completion(model=self.model, messages=self.messages)
