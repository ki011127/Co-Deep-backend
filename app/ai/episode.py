## 스토리 기반 연령대 별 길이가 다른 에피소드 생성 모델(저장)

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

class Episode():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.data = ""
        
    def read_file(self, file_path):
        absolute_path = os.path.normpath(os.path.abspath(file_path)).strip()
        print(f"Reading file: {absolute_path}")
        
        if not os.path.exists(absolute_path):
            print(f"File not found: {absolute_path}")
            return
        
        try:
            with open(absolute_path, 'r', encoding='utf-8') as json_file:
                self.data = json.load(json_file)
                # print("JSON Data:", self.data)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")
        
    def make_episode(self, age):
        ## Co-Deep-backend 에서 실행할 때는 아래의 경로를 사용
        self.read_file("app/data/conan/story3.json")
        
        prompt = f"""
            You are a model that makes episodes based on the basic story.
            The basic story will given in user's input.
            The basic story's format is as follows:
                case_development: the order of the story that contains incident, location, description, evidence
                suspects: the list of suspects that contains name, alibi, motive, evidence
                crime_tricks: the list of crime tricks that contains crime, method, motive, evidence
                culprit: name, age, occupation, motive, crimes
            You must create a episode based on the basic story and the user's age group.
            The younger the age group, the shorter the episode. The older the age group, the longer the episode.
            The younger the age group, the smaller the number of evidence and only important evidence should exist.
            The older the age group, the larger the number of evidence and there should be a variety of evidence that confuses the user.
            The younger the age group, the more cruel and dangerous the existing story should be converted into light and fun materials.
            The younger the age group, the more cruel and dangerous the description of the material should be avoided.
            You should keep in mind that you are an episode extraction model for developing learning games, and that dangerous or cruel materials for students should be adjusted by age group. This is a very important part.
            You have to make an episodes that contains description, evidence, suspects, crime tricks, and culprits based on the basic story.
            Each episode should contain 10~15 sentences. Please describe the episode in detail.
            You must follow the episode difference by age group. This is a very important part.
            You need to choose an important episode and create one that matches the length of the episode for your age group. It should be summarized well so that the story goes smoothly.
            In the last episode, the criminal must be arrested and the motive and method of the crime must be informed.
            The episodes you created should be clear on the basic story.
            The priorities to consider are the length of episode 1, number of clues 2, and risk consideration for number 3.
            I don't want you to use all the case development story. Just pick some important parts and make it into an episode.
            The episode difference by age group(Most important part!!)
                1. level 1: 4~5 episodes, intuitive, important, criminal evidence, importance of 4 points or higher evidence, light and fun materials, no cruel or dangerous materials
                2. level 2: 6~7 episodes, confusing and hard-to-find evidence, importance of 2 points or higher evidence, a story based on the original story, cruel and dangerous material is not direct, but indirectly labeled
                3. level 3: 7~9 episodes, more confusing and hard-to-find, importance of 1 points or higher evidence, difficult evidence, a story based on the original story, cruel and dangerous materials is allowed
            You must answer in English.
            User's age: {age}
            
            The output format should be as follows:
                Target Age: 14-16 years old
                Episode 1: Incident at Location
                Description of the incident
                Evidence collected:
                - Type: Description, importance: 4
        """
        
        assistant_content = """
            Target Age: 14-16 years old
            ### Episode 1: Nobukazu's Disappearance

            Returning to the mansion, they find that Takeda Nobukazu is missing. A search ensues but yields no trace of him. They expand their search to surrounding buildings, including an old warehouse on the property.

            ---

            ### Episode 2: The Gruesome Discovery

            The group breaks into the warehouse and finds Nobukazu’s body hanging from the ceiling like a spider's web. Conan and Heiji investigate thoroughly.
            
            **Evidence Collected:** 
            - Blow to the back of his head (importance: 4)
            - No exit except a small window (importance: 5)

            ---

            ### Episode 3: Investigating Further

            Conan and Heiji determine that Nobukazu died shortly after dinner. The locked-room scenario deepens their suspicion that this was a well-planned crime.

            **Evidence Collected:** 
            - Rusty nail (importance: 3)
            - Scattered flashlight and shoes (importance: 3)
            """
        
        messages = []
        messages.append({"role": "system", "content": prompt})
        
        all_data = {
            "case_development": self.data.get('case_development', []),
            "suspects": self.data.get('suspects', []),
            "crime_tricks": self.data.get('crime_tricks', []),
            "culprit": [self.data.get('culprit', {})]
        }

        for data_type, data_list in all_data.items():
            for item in data_list:
                if data_type == 'case_development':
                    incident_details = f"Incident {item['incident']} at {item['location']}:\n{item['description']}"
                    if item['evidence']:
                        evidence_list = "\n".join([f"- {e['type']}: {e['description']}, importance: {e['importance']}" for e in item['evidence']])
                        incident_details += f"\nEvidence collected:\n{evidence_list}"
                    messages.append({
                        "role": "user",
                        "content": incident_details
                    })
                elif data_type == 'suspects':
                    suspect_info = f"Name: {item['name']}\nAlibi: {item['alibi']}\nMotive: {item['motive']}"
                    if item['evidence']:
                        evidence_list = "\n".join([f"- {e['type']}: {e['description']}" for e in item['evidence']])
                        suspect_info += f"\nEvidence:\n{evidence_list}"
                    messages.append({
                        "role": "user",
                        "content": f"Suspect Details:\n{suspect_info}"
                    })
                elif data_type == 'crime_tricks':
                    crime_info = f"Crime: {item['crime']}\nMethod: {item['method']}\nMotive: {item['motive']}"
                    if item['evidence']:
                        evidence_list = "\n".join([f"- {e['type']}: {e['description']}" for e in item['evidence']])
                        crime_info += f"\nEvidence:\n{evidence_list}"
                    messages.append({
                        "role": "user",
                        "content": f"Crime Details:\n{crime_info}"
                    })
                elif data_type == 'culprit':
                    if item:
                        culprit_info = f"Name: {item['name']}\nAge: {item['age']}\nOccupation: {item['occupation']}\nMotive: {item['motive']}\nCrimes: {', '.join(item['crimes'])}"
                        messages.append({
                            "role": "user",
                            "content": f"Culprit Details:\n{culprit_info}"
                        })

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
        
        return response.choices[0].message.content

    
    
if __name__ == "__main__":
    episode = Episode()
    print(episode.make_episode(19))
    