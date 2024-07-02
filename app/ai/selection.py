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
            Full details is the full detail of the story that the each selection should be based on.
            You must create a selection that leads to the next detail story.
            You must create a selection that is based on the target detail.
            You must follow the selection difference by age group. This is a very important part.
            The maximum number of selections is 3.
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
    Heiji was on his way to the warehouse, following a tip he received about suspicious activities. The old building stood eerily silent as he approached it. His heart pounded with a mix of fear and determination. He knew Kazuha was in danger, and every second counted. As he pushed open the creaky door, he heard faint sounds coming from deep inside the warehouse.

    Navigating through the dimly lit space, Heiji's eyes scanned for any signs of movement. Suddenly, he spotted Kazuha tied up with fishing line in a corner. Her wrists were bound tightly, and her face showed signs of distress. But what horrified him the most was the noose around her neck, set up to make it look like she was about to be hanged. Without wasting a moment, Heiji rushed to her side.

    "Hang on, Kazuha! I'm here," Heiji whispered urgently as he began working on the knots. The fishing line cut into his fingers, but he ignored the pain. Kazuha's eyes filled with tears of relief as she saw Heiji. She tried to speak, but her voice was weak from fear and exhaustion. "It's going to be okay," Heiji reassured her, focusing on freeing her from the deadly trap.

    After what felt like an eternity, Heiji finally managed to untie Kazuha. He carefully removed the noose from around her neck and helped her stand up. "Can you walk?" he asked gently. Kazuha nodded shakily, leaning on him for support. They needed to get out of there quickly before whoever did this returned. As they made their way towards the exit, Heiji kept a vigilant eye on their surroundings.

    Once outside, they both took a moment to catch their breath. The cool night air felt refreshing after the tense situation inside the warehouse. "Thank you, Heiji," Kazuha said softly, her voice still trembling. "I don't know what would have happened if you hadn't come." Heiji gave her a reassuring smile and replied, "You're safe now, that's all that matters." They knew they had to report this incident and find out who was behind such a cruel act, but for now, they were just grateful to be alive and together.
    """
    
    target_detail = "Navigating through the dimly lit space, Heiji's eyes scanned for any signs of movement. Suddenly, he spotted Kazuha tied up with fishing line in a corner. Her wrists were bound tightly, and her face showed signs of distress. But what horrified him the most was the noose around her neck, set up to make it look like she was about to be hanged. Without wasting a moment, Heiji rushed to her side."
    
    selection.make_selection(target_detail, full_details, 15)
    