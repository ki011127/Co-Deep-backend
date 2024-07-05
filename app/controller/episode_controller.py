from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class EpisodeController:  
    async def count_clues(self, episode_id):
        count = await mongodb.db.clues.count_documents({"episode_id": episode_id})
        return count

    async def get_episodes(self, story_id, level):
        print(story_id)
        episodes = await mongodb.db.episodes.find({"story_id": story_id, "level": level},
            {"_id": 1, "story_id": 1, "level": 1, "order": 1, "title": 1, "clue_ids": 1, "img": 1, "description": 1}
        ).to_list(length=None)
        for i in range(len(episodes)):
            episodes[i]["_id"] = str(episodes[i]["_id"])
        print(episodes)
        return episodes
    
    async def episode_order(self, story_id, level, order):
        episodes = await mongodb.db.episodes.find({"story_id": story_id, "level": level},
            {"_id": 1, "story_id": 1, "level": 1, "order": 1, "title": 1, "clue_ids": 1, "img": 1, "description": 1}
        ).to_list(length=None)
        s = len(episodes)
        
        for i in range(s):
            episodes[i]["_id"] = str(episodes[i]["_id"])
            num_of_clues = await self.count_clues(episodes[i]["_id"])
            if episodes[i]["order"] == order:
                episodes[i]["num_of_episodes"] = s
                episodes[i]["num_of_clues"] = num_of_clues
                return episodes[i]