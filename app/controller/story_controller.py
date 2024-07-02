from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class StoryController:    
    async def get_story(self):
        # existing_user = await mongodb.engine.find_one(Users, Users.uuid == uuid)
        stories = await mongodb.db.stories.find({}, {"_id": 0, "story_id": 1,"title": 1, "description": 1}).to_list(length=None)
        print(stories)
        return stories