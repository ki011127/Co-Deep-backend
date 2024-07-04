from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class ClueController:    
    async def get_clue(self, id):
        print(id)
        clue = await mongodb.db.clues.find_one({"_id": ObjectId(id)}, {"_id": 1, "name": 1, "description": 1, "img":1})
        clue['_id'] = str(clue['_id'])
        
        return clue