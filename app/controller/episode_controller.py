from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class EpisodeController:    
    async def get_episodes(self, story_id, age):
        print(story_id)
        episodes = await mongodb.db.episodes.find({"story_id": story_id, "age": age},
            {"_id": 1, "story_id": 1, "age": 1, "order": 1, "title": 1, "clue_ids": 1, "img": 1, "description": 1}
        ).to_list(length=None)
        for i in range(len(episodes)):
            episodes[i]["_id"] = str(episodes[i]["_id"])
        print(episodes)
        return episodes