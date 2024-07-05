from openai import OpenAI

import time
from typing import List
from pydantic import BaseModel, Field
import os
import pandas as pd
from dotenv import load_dotenv
import json

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class WrongSelection():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def create_detail(self, selection, content):
        prompt = f"""
            You are a model that processes when the user enters the wrong option.
            You should create a natural story based on the story and the choice user choose.
            You should be done simply in a sentence or two.

            base story:
                {content}

        """
        print(prompt)
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": selection },
            ],
            temperature=0.8,
            max_tokens=2000,
            top_p=0.5,
            frequency_penalty=0.2,
            presence_penalty=0.8,
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content

if __name__ == "__main__":
    wrongSelection = WrongSelection()
    
    ## detail.py 에서 생성된 데이터
    content = "Inside the apartment, they found Raisaku lying on the floor. His coffee cup was next to him. It looked like he might have poisoned himself by drinking the coffee. Conan started to think about what could have happened."
    selection = "Leave the apartment and check the mailbox for any letters."
    #Wrong_Story = "Conan decided to leave the apartment and check the mailbox for any letters. To his surprise, he found an envelope addressed to Raisaku with no return address, hinting at a deeper mystery.

    wrongSelection.create_detail(selection, content)
