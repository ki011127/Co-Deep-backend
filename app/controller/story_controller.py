from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class StoryController:    
    async def get_story(self):
        # existing_user = await mongodb.engine.find_one(Users, Users.uuid == uuid)
        stories = await mongodb.db.stories.find({}, {"_id": 1, "title": 1, "description": 1, "subtitle": 1}).to_list(length=None)
        for i in range(len(stories)):
            stories[i]["_id"] = str(stories[i]["_id"])
        print(stories)
        return stories