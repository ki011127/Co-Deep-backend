from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class ClueController:    
    async def check_clue(self, episode_id, name, num_of_try, order):
        clue = await mongodb.db.clues.find_one({"episode_id": episode_id, "order":order})
        if clue:
            clue['_id'] = str(clue['_id'])
        if num_of_try == 1:
            if clue:
                if clue['name'].lower()==name.lower():
                    return {"result": "success", "clue": clue}
                else:
                    clue = {"detail_id" : clue['detail_id']}
                    return { "result": "wrong", "clue": clue}
            else:
                return clue
        elif num_of_try == 2:
            if clue:
                if clue['name'].lower()==name.lower():
                    return {"result": "success", "clue": clue}
                else:
                    return { "result": "wrong", "clue": clue}
            else:
                return clue
        
        return clue