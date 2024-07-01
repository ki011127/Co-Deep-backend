## 에피소드를 구체화하여 연령대 별 스토리를 생성하는 모델

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

class Level():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        
    def make_korean_to_english(self, query, age):
        
        prompt = f"""
            You are a translator who translates Korean into English by adjusting the difficulty level by age group.
            You have to translate based on the user's input.
            You should keep in mind that this translation is intended for Koreans. It's not for English-speaking students, but for Koreans.
            It's not just a direct translation, but you have to understand the content and omit or add it based on it.
            You have to create and add several new sentences based on the existing content.
            In particular, if the target is over 14 years old, the entire sentence must go over 15 lines.
            You must translate the user's input into English based on the user's age group.
            The level of difficulty by age group
                1. 5-9 years old: very easy words, basic grammar, use no more than 8 words per sentence, full length no more than 3 sentences
                2. 10-13 years old: elementary school words, basic grammar, use no more than 13 words per sentence, total length not more than 5 sentences
                3. 14-16 years old: words for middle school students, applied grammar, use no more than 20 words per sentence, total length is more than 5 no more than 10 sentence
                4. 17-19 years old: words for high school students, advanced grammar, use words of no more than 30 words per sentence, the total length is more than 10 no more than 20 sentences
            You must answer in English.
            User's input: {query}
            User's age: {age}
        """
        
        assistant_content = """
            Episode 1: News of Heiji Hattori's Restaurant Opening

            Conan: "Heiji, what's the good news?"

            Heiji Hattori: "Conan, I finally opened that dream restaurant in Osaka! You have to come!"

            Conan: "Really? Congratulations, Heiji! I'll leave tomorrow."

            Conan decides to accept Heiji Hattori's invitation and head to Osaka. He prepares to leave, excited to see the new restaurant in Osaka.

            Choices:

            "Great, I'll take the first train tomorrow."
            "Osaka is always fun. See you tomorrow!"
            "I'm not sure if I can go because I'm busy, but I'll try."
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query },
                {"role": "assistant", "content": assistant_content}
            ],
            temperature=0.8,
            max_tokens=2000,
            top_p=0.8,
            frequency_penalty=0.4,
            presence_penalty=0.8,
        )
        
        return response.choices[0].message.content
    
    def make_english_to_english(self, query, age):
            
        prompt = f"""
            You are a model that controls the difficulty of each age group based on the basic story.
            You have to translate based on the user's input.
            You should keep in mind that this translation is intended for Koreans. It's not for English-speaking students, but for Koreans.
            It's not just a direct translation, but you have to understand the content and omit or add it based on it.
            You have to create and add several new sentences based on the existing content.
            In particular, if the target is over 14 years old, the entire sentence must go over 15 lines.
            You must translate the user's input into English based on the user's age group.
            The level of difficulty by age group
                1. 5-9 years old: very easy words, basic grammar, use no more than 8 words per sentence, full length no more than 3 sentences
                2. 10-13 years old: elementary school words, basic grammar, use no more than 13 words per sentence, total length not more than 5 sentences
                3. 14-16 years old: words for middle school students, applied grammar, use no more than 20 words per sentence, total length is more than 5 no more than 10 sentence
                4. 17-19 years old: words for high school students, advanced grammar, use words of no more than 30 words per sentence, the total length is more than 10 no more than 20 sentences
            You must answer in English.
            User's input: {query}
            User's age: {age}
        """
        
        assistant_content = """
            Episode 1: News of Heiji Hattori's Restaurant Opening

            Conan: "Heiji, what's the good news?"

            Heiji Hattori: "Conan, I finally opened that dream restaurant in Osaka! You have to come!"

            Conan: "Really? Congratulations, Heiji! I'll leave tomorrow."

            Conan decides to accept Heiji Hattori's invitation and head to Osaka. He prepares to leave, excited to see the new restaurant in Osaka.

            Choices:

            "Great, I'll take the first train tomorrow."
            "Osaka is always fun. See you tomorrow!"
            "I'm not sure if I can go because I'm busy, but I'll try."
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query },
                {"role": "assistant", "content": assistant_content}
            ],
            temperature=0.8,
            max_tokens=2000,
            top_p=0.8,
            frequency_penalty=0.4,
            presence_penalty=0.8,
        )
        
        return response.choices[0].message.content
    
    def make_story(self, query, age):
        
        content = f"""
        The story is created according to the story flow, and five to six episodes are created per story flow sentence. You must create one episode, print out each episode, and wait for the user's choice. If the story flow is given in 7 sentences, 35 to 42 episodes should be made. The main character has Conan as the first person. 
        When creating options, you provide them in the form of "answer" with half the probability and no impact on the story at all. In this case, it is desirable to ask the main character something about the previous question (for example, answers such as "good," "just so," and "hum..." to the question of how the food is). And the other half is written in the form of "action" to have a slight impact on the story, although it affects it.

        If the user recorded more than half of the decisive clues before the culprit was identified, the story proceeds as the existing story flow, and if more than half of the users failed to record, Conan failed to identify the culprit and the case fell into a mystery.
        """
        
        input = f"""
        Story flow:
        - Conan decides to visit after hearing the news of the opening of a restaurant in Osaka from Heiji Hattori.
        - You find a group of famous sports stars in a restaurant.
        - Newspaper reporter Ed McKay appears and causes conflict by revealing the stars' past.
        - Ed McKay is found murdered.
        - Conan and friends investigate the case, and three suspects exist.
        - Conan identifies the culprit, Ray Curtis, through several clues.
        - Ray Curtis explains the motive for killing Ed and confesses.

        Clue:
        Fire in the right end of the first floor (Clue 1)
        Gunpowder reaction in shoes (clue 2)
        Dying Message (Clue 3)
        Water on the towel (Clue 4)
        a pin on a soccer ball (clue 5)

        Crime Tricks:
        Making an alibi using a mop and a soccer ball, killing Ed by making it look like he was on the first floor.

        Crimestoppers Name:
        Ray Curtis
        """
            
        prompt = f"""
            The story is created according to the story flow, and five to six episodes are created per story flow sentence. You must create one episode, print out each episode, and wait for the user's choice. If the story flow is given in 7 sentences, 35 to 42 episodes should be made. The main character has Conan as the first person. 
            When creating options, you provide them in the form of "answer" with half the probability and no impact on the story at all. In this case, it is desirable to ask the main character something about the previous question (for example, answers such as "good," "just so," and "hum..." to the question of how the food is). And the other half is written in the form of "action" to have a slight impact on the story, although it affects it.

            If the user recorded more than half of the decisive clues before the culprit was identified, the story proceeds as the existing story flow, and if more than half of the users failed to record, Conan failed to identify the culprit and the case fell into a mystery.
        
        
            You are a model that controls the difficulty of each age group based on the basic story.
            You have to translate based on the user's input.
            You should keep in mind that this translation is intended for Koreans. It's not for English-speaking students, but for Koreans.
            It's not just a direct translation, but you have to understand the content and omit or add it based on it.
            You have to create and add several new sentences based on the existing content.
            In particular, if the target is over 14 years old, the entire sentence must go over 15 lines.
            You must translate the user's input into English based on the user's age group.
            The level of difficulty by age group
                1. 5-9 years old: very easy words, basic grammar, use no more than 8 words per sentence, full length no more than 3 sentences
                2. 10-13 years old: elementary school words, basic grammar, use no more than 13 words per sentence, total length not more than 5 sentences
                3. 14-16 years old: words for middle school students, applied grammar, use no more than 20 words per sentence, total length is more than 5 no more than 10 sentence
                4. 17-19 years old: words for high school students, advanced grammar, use words of no more than 30 words per sentence, the total length is more than 10 no more than 20 sentences
            You must answer in English.
            User's input: {query}
            User's age: {age}
        """
        
        assistant_content = """
            Episode 1: News of Heiji Hattori's Restaurant Opening

            Conan: "Heiji, what's the good news?"

            Heiji Hattori: "Conan, I finally opened that dream restaurant in Osaka! You have to come!"

            Conan: "Really? Congratulations, Heiji! I'll leave tomorrow."

            Conan decides to accept Heiji Hattori's invitation and head to Osaka. He prepares to leave, excited to see the new restaurant in Osaka.

            Choices:

            "Great, I'll take the first train tomorrow."
            "Osaka is always fun. See you tomorrow!"
            "I'm not sure if I can go because I'm busy, but I'll try."
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query },
                {"role": "assistant", "content": assistant_content}
            ],
            temperature=0.8,
            max_tokens=2000,
            top_p=0.8,
            frequency_penalty=0.4,
            presence_penalty=0.8,
        )
        
        return response.choices[0].message.content
    
    
if __name__ == "__main__":
    level = Level()
    
    korean_tmp = f"""
        에피소드 1: 핫토리 헤이지의 레스토랑 개업 소식
        코난: "핫토리, 무슨 좋은 일이 있는 거야?"

        핫토리 헤이지: "코난, 드디어 그 꿈에 그리던 레스토랑을 오사카에 열게 됐어! 꼭 와줘야 해."

        코난: "정말? 축하해, 헤이지! 내일 바로 출발할게."

        코난은 핫토리 헤이지의 초대에 응하며 오사카로 향하기로 결심한다. 오사카의 새로운 레스토랑이 어떤 모습일지 기대감을 안고 떠날 준비를 한다.

        선택지:

        "좋아, 내일 첫 기차로 갈게."
        "오사카는 언제 가도 즐거워. 내일 보자!"
        "일정이 바빠서 갈 수 있을지 모르겠어, 하지만 해볼게."
    """
    
    english_tmp = f"""
        Episode 1: Hattori Hage's restaurant opening news
        Conan: "Hottori, what's the good thing?"

        Hattori Hage: "Conan, I'm finally opening my dream restaurant in Osaka! You have to come."

        Conan: "Really? Congratulations, Hage! I'll leave tomorrow."

        Conan decides to head to Osaka, accepting Hattori Hage's invitation. Get ready to leave with anticipation of what Osaka's new restaurant will look like.

        Options:

        "Okay, I'll take the first train tomorrow."
        "I'm always happy to go to Osaka. See you tomorrow!"
        "I'm busy with my schedule, so I don't know if I can go, but I'll try."
    """
    
    # print("Korean to English")
    # print(level.make_korean_to_english(korean_tmp, 18))
    
    print("English to English")
    print(level.make_english_to_english(english_tmp, 18))