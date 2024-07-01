from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class ClueController:    
    async def get_clue(self, clue_id):
        clue = await mongodb.db.clues.find_one({"clue_id": clue_id}, {"_id": 0, "clue_id": 1,"name": 1, "description": 1, "img":1})
        print(clue)
        return clue