import os
import openai
class Chatbot:
    """
    This class handles everything related to the chatgpt bot

    Attributes:
        self.system_msg : string
            - a system message for the chatbot. It tells it what its supposed to do
        self.messages : list 
            - messages that are stored for the chatbot so it can infer on them.
    """
    def __init__(self,system_message):
        self.system_msg = system_message
        self.messages = [
                {"role": "system", "content": self.system_msg},
            ]

    def ask_gpt3(self,question):
        self.messages.append({"role": "user", "content": question})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        assistant_msg = response['choices'][0]['message']['content']
        self.messages.append({"role": "assistant", "content": assistant_msg})
        return assistant_msg






