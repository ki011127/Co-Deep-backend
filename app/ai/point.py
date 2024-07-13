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



conan = """the method of committing a crime
            The real killer was not Somei. Unlike Conan, a famous detective who starts off by implying the killer, this episode has a twist that the suspect who seemed to be the killer was not the real culprit. Both Conan and the police suspected Somei Shogo from the beginning, and he was the only suspect, and the true culprit was not even featured throughout the episode[3] and was not treated seriously.

            The real culprit was Maiko Kuzumi. The reason it was nowhere to be seen in the scene was because he killed himself by throwing himself through a window immediately after the crime. The true criminal who was at the scene at the time of the crime escaped the scene by jumping through a window rather than through a door, and if the person who tried to hide something by fabricating evidence is a person separate from the criminal, a case that seemed like an impossible crime can be easily solved.

            The motive for this case is one of the criminals of Detective Conan. Somei did not reveal that Raisaku was targeting for her for Maico and threatening to not give her work to the company unless she gave her up, but Maico was already aware. After Somei refused to hand over Maico to him on the phone on the way home after a meeting with Detective Mori, Raisaku retaliated and cut off all work he had given to the production company of Someine, and overturned the program he promised to do with Detective Mori, making Somei look emaciated and his health deteriorated due to financial difficulties. Nevertheless, Somei did not disclose the fact to Maico, but when she realized that Raisaku had threatened him, she decided to buy a cake and visited Raisaku the next day to poison his coffee to kill him.

            After the crime, Maiko went straight to the balcony and committed suicide, and just before committing suicide, he called his beloved Somei and confessed his love for him, and died by jumping to the ground. Upon arriving at the scene in a hurry, Somei found Maiko's body in the parking lot and hid it in the trunk of his car.[6] The reason why Somei manipulated the coffee stand to hide the fact that Maiko visited and disguised himself as a real criminal was because he did not want to disgrace the deceased Maiko as a murderer, so he wanted to be framed instead. In other words, it is a truly unfortunate incident in which lovers who like each other fell to the abyss at one point because of the victim's dark feelings.

            Somay appeals to the police to arrest him because he is the culprit, but if Conan, who borrowed Kogoro's voice, is caught now, he soothes him about what will happen to Maiko's body in the trunk, and Somay breaks down sobbing so much that he can't control himself. The case ends when Conan and Ran look at him sadly and Megure, who was expressing regret, helps him to his feet. Somay is taken to the police station on charges of false testimony and evidence manipulation[7] and he is desperate to take his eyes off Maiko's body, which is carried away in an ambulance until the last minute when he gets into a police car.

            It is Somei who manipulated the evidence by placing a coffee stand, but the reason why the coffee stand was placed later is important. Conan sees a strange mark under the stand and suspects that something is on this mark and hides it with a stand, but the key to this evidence manipulation was to hide that there was not only one Raisaku at the scene at the time of the crime, but the culprit was invited as a guest. Conan gets to the bottom of the cake on the plate by the smell of the coffee left in the pot and pencil holder cups, not by one piece. Originally, there were two plates of two cakes and two coffee cups on the table. Somei, who first burst into the scene, spilled the remaining coffee from the criminal's coffee cup, put the writing instrument in a pot, placed it on the desk side, disguised it as a pencil holder, and put the criminal's cake together with the victim's cake on one plate, disguised it to look like a single serving, and then laid the plate under the cup to look like a coffee stand. In other words, the coffee stand was not placed to hide something, but to hide that there was another person on the spot and to produce as if Raisaku was alone.

            Then the question of where the fork was left remains, and Somei, who has been pretending that he is not the criminal until now, watches the whole situation and takes out the fork he hid in his jacket to reveal his crime. Conan, who already knows the truth, begins a reasoning by borrowing Kogoro's voice, saying that the criminal has fled to heaven."""

homes = """Holmes stopped by the registry office to investigate the Stoner family's situation before heading to Stoke Moran. The investigation discovered that the Stoner sisters' mother left a legacy, but if the sisters married, Dr. Grimsby Roylott would not be able to receive a penny. In other words, Dr. Grimsby Roylott had enough motivation to harm the sisters. Then I met Helen at Stoke Moran. Holmes told Helen that he had met Dr. Grimsby Roylott, and Helen finally found out that she had been followed.

            Holmes made a few strange discoveries when he looked around the scene of the incident. On the wall of Julia's room that Helen is currently using, there was a hole that connects to the next room. It was Dr. Grimsby Roylott's room. Grimsby Roylott was such a cocoon that he enjoyed strong cigars, which is why Julia smelled them every day. And the bigger question was the strange row next to the hole. Helen testified that she knew that the row was used by a doorbell and was connected to the housekeeper's room, but her sister had never used it. However, Holmes pulled the rope and made no sound. It turned out that the rope was just hanging from a hook on the wall. What is this rope for? Also, the bed was fixed so that it could not move.

            Then, when I entered Dr. Grimsby Roylott's room next door, I noticed a large safe. Then I saw a plate of milk. Holmes replied that Helen wouldn't have a cat when the doctor asked Helen if she had a cat. Other than that, I saw a whip with a hook. Holmes learned the truth of the incident from these facts.
            
            The culprit was Dr. Roylott. He was living off the pension that came from his wife's inheritance, but if any of the daughters were married and the pension was passed on to them, life would be difficult. So when Julia married, she sent an Indian viper into a vent that led between the rooms, and Julia was bitten by a viper and killed. When Julia died, the whistle was the sound of the doctor trying to deal with the snake, and the sound of the metal was the sound of the safe where the snake was kept. Julia's statement before she died as "a zebra" was a misunderstanding of the spotted snake as a string in the dark.

            At first, Holmes suspected that Julia might have seen the Gypsies' towels before she died and said, "Specked band," but when he actually looked into the room and felt the suspicion, he thought of the snake and guessed how to commit the crime."""
y = """"""
lady = """"""
class Point():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.messages = []

    def make_prompt(self, content, story_name):
        input = None
        if story_name == "conan":
            input = conan
        elif story_name == "homes":
            input = homes
        elif story_name == "y":
            input = y
        else:
            input = lady
        prompt = f"""
            You are a model who evaluates the score of an answer to a question.
            The user will enter the question and answer to you together. Wait for the input.
            Please rate the appropriateness of the answer to the question as 0-5 points.
            Please evaluate the answer based on the given story.
            The output should only output the score.

            Story:
            {input}

            based on the score : 
                5: when the answers are somewhat consistent based on the story.
                1~4: If your answer is sparse with details or comprehensive, give 1 to 4 points depending on the level.
                0: Requesting hints, saying I don't know, answers that don't match the story.
        """
        self.messages = []
        self.messages.append({"role": "system", "content": prompt})
        self.messages.append({"role": "user", "content":content})

    def point(self, content, story_name):
        #content = "q : Who do you think is the real killer in this case?\na : maiko"
        self.make_prompt(content, story_name)
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages,
            temperature=0.6,
            max_tokens=2000,
            top_p=0.5,
            frequency_penalty=0.2,
            presence_penalty=0.8,
        )
        #print(response.choices[0].message.content)
        return response.choices[0].message.content
    
    
    
if __name__ == "__main__":
    point = Point()
    print(point.point("1"))