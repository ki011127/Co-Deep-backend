from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class StoryController:    
    async def get_story(self, age):
        age = int(age)
        ver = 0
        if age < 14:
            ver = 1
        elif age < 17:
            ver = 2
        else:
            ver = 3
        # existing_user = await mongodb.engine.find_one(Users, Users.uuid == uuid)
        stories = await mongodb.db.stories.find({}, {"_id": 1, "title": 1, "description": 1, "subtitle": 1}).to_list(length=None)
        for i in range(len(stories)):
            print(stories[i]["_id"])
            first_ep = await mongodb.db.episodes.find({"story_id": str(stories[i]['_id']), "order": 1, "age": ver}).to_list(length=None)
            if first_ep:
                first_ep[0]["_id"] = str(first_ep[0]["_id"])
                stories[i]['first_ep'] = first_ep
            else:
                stories[i]['first_ep'] = [
                    {
                    "_id": "id",
                    "story_id": "story_id",
                    "age": 1,
                    "clue_ids": [],
                    "img": "이미지url",
                    "order": 1,
                    "title": "Homes",
                    "description": "description"
                    }
                ]
        for i in range(len(stories)):
            stories[i]["_id"] = str(stories[i]["_id"])
        print(stories)
        return stories