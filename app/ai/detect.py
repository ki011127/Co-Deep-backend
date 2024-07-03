## 용의자 심문 모델
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

class Detect():
    def __init__(self, story):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.story = story
        self.detect_messages = self.get_messages(story)
        
    def get_messages(self, story):
        ## Co-Deep-backend 에서 실행할 때는 아래의 경로를 사용
        file_path = "data/" + story + "/detect/detect.json"
        absolute_path = os.path.normpath(os.path.abspath(file_path)).strip()
        print(f"Reading file: {absolute_path}")
        
        if not os.path.exists(absolute_path):
            print(f"File not found: {absolute_path}")
            return
        
        try:
            with open(absolute_path, 'r', encoding='utf-8') as json_file:
                # self.episodes = json.load(json_file)
                return json.load(json_file)
                # print("JSON Data:", self.data)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")
        
    def detect(self, clues):
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
        """
        messages = []
        messages.append({"role": "system", "content": prompt})
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
    detect = Detect("conan")
    print(detect.detect(12))