## 에피소드를 구체화하여 연령대 별 세부 디테일을 생성하는 모델(실시간)

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

class Detail():
    def __init__(self, story, age):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.age = age
        self.story = story
        self.episodes = self.get_episodes(story, age)
        
    def get_episodes(self, story, age):
        ## story 는 data 폴더 안의 conan, sherlock 등을 의미
        ver = 0
        if age < 14:
            ver = 1
        elif age < 17:
            ver = 2
        else:
            ver = 3
        
        ## Co-Deep-backend 에서 실행할 때는 아래의 경로를 사용
        file_path = "app/data/" + story + "/episode/" + str(ver) + ".json"
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
        
    def make_story(self, episode, evidences=None, has_evidence=False):
        
        prompt = f"""
            You are a model that controls the difficulty of each age group based on the basic episode.
            You have to convert based on the user's input.
            You should keep in mind that this convert is intended for Koreans. It's not for English-speaking students, but for Koreans.
            It's not just a direct conversion, but you have to understand the content and omit or add it based on it.
            You should create a story based on the existing content.
            Include evidence naturally.
            I hope there is no direct explanation of the evidence.
            You must translate the user's input into English based on the user's age group.
            The level of difficulty by age group (Sentence structure, Change vocabulary, grammar, number of words, and words as stated below based on age.)
                1. 10-13 years old: elementary school words, basic grammar, use no more than 13 words per sentence, total length not more than 5 sentences per paragraph, no more than 3 paragraphs, very easy vocabulary, very easy sentence structure
                2. 14-16 years old: words for middle school students, applied grammar, use no more than 20 words per sentence, total length is more than 5 no more than 10 sentence, no more than 4 paragraphs, easy vocabulary, easy sentence structure
                3. 17-19 years old: words for high school students, advanced grammar, use words of no more than 30 words per sentence, the total length is more than 10 no more than 20 sentences, no more than 5 paragraphs, a moderate level of vocabulary, a moderate level of sentence structure
            You must answer in English.
            
            Format the output as follows:
                Title: {episode['episode']} {episode['title']}
                Age Group: [Age Group]
                Story:
                [Generated Story]
            
            Basic Episode data is as follows:
                Episode description: {episode['description']}
                User's age: {self.age}
        """
        
        # if culprit_details:
        #     prompt += f"\n\n\tAdditionally, include the following evidence in the story:\n"
        #     prompt += f"\tName: {culprit_details['name']}\n"
        #     prompt += f"\tAge: {culprit_details['age']}\n"
        #     prompt += f"\tOccupation: {culprit_details['occupation']}\n"
        #     prompt += f"\tMotive: {culprit_details['motive']}\n"
        #     prompt += "\tCrimes: " + ", ".join(culprit_details['crimes']) + "\n"

        if has_evidence:
            prompt += f"\n\n\tAdditionally, include the following evidence in the story:\n"
            for i in range(len(evidences)):
                prompt += f"\tevidence {i+1}: {evidences[i]}\n"
            prompt += "\n\tWrite a detailed story based on the above information."
            prompt += "\n\tDon't feature evidences in the first paragraph."
        else:
            prompt += "\n\tWrite a detailed story in no more than 2 paragraphs based on the above information."
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": episode['description'] },
            ],
            temperature=0.8,
            max_tokens=2000,
            top_p=0.5,
            frequency_penalty=0.2,
            presence_penalty=0.8,
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    
    def run(self, episode_number):
        ## 에피소드 번호 기반으로 디테일 생성
        last_episode_number = self.episodes['episodes'][-1]['episode']
        
        for episode in self.episodes['episodes']:
            if episode['episode'] == episode_number:
                has_evidence = 'evidence_collected' in episode and len(episode['evidence_collected']) > 0
                evidences = []
                if(has_evidence):
                    evidences = episode['evidence_collected']
                #culprit_details = self.episodes['culprit_details'] if episode['episode'] == last_episode_number else None
                story =  self.make_story(episode, evidences, has_evidence)
                return f"Episode {episode['episode']}: {episode['title']}\n\n{story}\n\n{'='*50}\n"
    
if __name__ == "__main__":
    detail = Detail("homes", 19)
    
    detail.run(7)
    
    