from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class EpisodeController:    
    async def get_episodes(self, story_id, age):
        print(story_id)
        episodes = await mongodb.db.episodes.find({"story_id": story_id, "age": age},
            {"_id": 0, "episode_id":1,"story_id": 1, "age": 1, "order": 1, "content": 1, "clue_ids": 1, "img": 1}
        ).to_list(length=None)
        print(episodes)
        return episodes