from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo
from ai.wrong_selection import WrongSelection
import os
import json

class DetailController:
    async def get_details_json(self, story, level):
        ## Co-Deep-backend 에서 실행할 때는 아래의 경로를 사용
        file_path = "data/" + story + "/detail/" + str(level) + ".json"
        print(file_path)
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
    

    async def get_detail(self, episode_id, user_id):
        details = await mongodb.db.details.find({"episode_id": episode_id, "user_id": user_id},
            {"_id": 1, "episode_id":1,"content": 1, "user_id": 1, "selection_id": 1,"created_at": 1}
        ).to_list(length=None)
        print(details)
        return details
    

    async def put_detail(self, episode_id, user_id, level, story_name, order, created_at):
        data = await self.get_details_json(story_name, level)
        episode_details = [detail for detail in data["details"] if detail["espisode_id"] == episode_id]
        content = ""
        selection_id = []
        if 0 <= order < len(episode_details):
            target_detail = episode_details[order]
            content = target_detail.get("content", "")
            selection_id = target_detail.get("selection_id", None)
            print(f'Content: {content}')
            print(f'Selection ID: {selection_id}')
        else:
            print(f'Target index {order} is out of range.')

        detail = {
            "episode_id": episode_id,
            "content": content,
            "user_id": user_id,
            "selection_id": selection_id,
            "created_at": created_at,
        }
        details = await mongodb.db.details.insert_one(detail)
        return {
            "content": content,
            "selection_id": selection_id,
            "num_of_details": len(episode_details)
        }
    
    async def wrong_detail(self, episode_id, user_id, selection, content, created_at):
        wrongSelection = WrongSelection()
        content = "Inside the apartment, they found Raisaku lying on the floor. His coffee cup was next to him. It looked like he might have poisoned himself by drinking the coffee. Conan started to think about what could have happened."
        selection = "Leave the apartment and check the mailbox for any letters."
        value = wrongSelection.create_detail(selection, content)
        detail = {
            "episode_id": episode_id,
            "content": content,
            "user_id": user_id,
            "selection_id": [],
            "created_at": created_at,
        }
        details = await mongodb.db.details.insert_one(detail)
        return {
            "content": value
        }
    
    async def get_all_detail(self, episode_id):
        print(episode_id)
        details = await mongodb.db.details.find({"episode_id": episode_id},
            {"_id": 1, "episode_id":1,"content": 1}
        ).to_list(length=None)
        print(details)
        s = len(details)
        for i in range(s):
            details[i]["_id"] = str(details[i]["_id"])
        return details