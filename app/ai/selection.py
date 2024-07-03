## 스토리 기반 선택지 생성 모델(저장..?)

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

class Selection():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def make_selection(self, target_detail, full_details, age):
        
        prompt = f"""
            You are a model that makes selections based on the basic detail story.
            The selection you made will be used to make next detail story.
            The basic detail story will given in user's input.
            You must create a selection based on the basic story and the user's age group.
            Target detail is the detail of the story that the user wants to create a selection.
            Full details is the full detail of the story that the correct selection should be based on.
            You must follow the selection difference by age group. This is a very important part.
            The maximum number of selections is 3.
            You must create one selection that leads to the target detail's next detail story and is based on the target detail.
            You must create two selections that are out of the context of the story.
            The selection difference by age group(Most important part!!)
                1. 5-9 years old: under 10 words of each selection, simple and easy to understand
                2. 10-13 years old: over 10 under 15 words of each selection, simple and easy to understand
                3. 14-16 years old: over 15 under 20 words of each selection, harder and more complex words and sentences
                4. 17-19 years old: over 20 under 25 words of each selection, harder and more complex words and sentencess
            You must answer in English.
            Target Detail that selection should be made: {target_detail}
            Full Details: {full_details}
            User's age: {age}
            
            The output format should be as follows:
                Target Age: 14-16 years old
                Episode 1: Incident at Location
                Detail: Description of the detail
                Selections:
                    1. Selection 1
                    2. Selection 2
                    3. Selection 3
                    
            Example of selection:
                1. Examine the knife on the desk
                2. Hear more of Kazuha's testimony
                3. There's nothing more to investigate, so move on to the next scene

        """
        
        messages = []
        messages.append({"role": "system", "content": prompt})
        
        messages.append({"role": "user", "content": f"Target Detail: {target_detail}"})
        messages.append({"role": "user", "content": f"Full Details: {full_details}"})
        messages.append({"role": "user", "content": f"User's age: {age}"})
        # messages.append({"role": "assistant", "content": assistant_content})
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.6,
            max_tokens=2000,
            top_p=0.5,
            frequency_penalty=0.2,
            presence_penalty=0.8,
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content

    
    
if __name__ == "__main__":
    selection = Selection()
    
    ## detail.py 에서 생성된 데이터
    full_details = """
    Conan looked around the room carefully. He saw a fork and a cake plate on the table. This made him think that someone else was with Raisaku before he died. It didn't look like a simple suicide anymore.

    Then, Conan found two coffee cups and plates on another table. This showed that two people were present in the room. Additionally, Conan thought that somei might have evidence of the case.

    Next, Conan checked Somei's jacket. He found a hidden fork inside it. Now, Conan was sure that Raisaku did not die alone.

    """
    
    target_detail = "Then, Conan found two coffee cups and plates on another table. This showed that two people were present in the room. Additionally, Conan thought that somei might have evidence of the case."
    
    selection.make_selection(target_detail, full_details, 15)
    