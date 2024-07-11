from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class ClueController:    
    async def check_clue(self, episode_id, name, order):
        clue = await mongodb.db.clues.find_one({"episode_id": episode_id, "order":order})
        if clue:
            clue['_id'] = str(clue['_id'])
        if clue:
            names = clue['sub'].split(',')
            for sub_name in names:
                if sub_name.lower() == name.lower():
                    return {"result": "success", "clue": clue}
            return { "result": "wrong", "clue": clue}
        else:
            return clue
    
    async def get_user_clues(self, story_id, name, level):
        clue_list = await mongodb.db.points.find({"story_id": story_id, "level": level, "name": name, "is_detect":0},{"_id": 0, "point": 1, "clue":1}).to_list(length=None)
        return clue_list