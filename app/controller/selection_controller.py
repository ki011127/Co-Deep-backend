from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class SelectionController:    
    async def get_selections(self, selection_id):
        for i in range(len(selection_id)):
            selection_id[i] = ObjectId(selection_id[i])
        selections = await mongodb.db.selections.find(
        {"_id": {"$in": selection_id}},
        {"_id": 1, "clue_id": 1, "content": 1, "correct": 1}
        ).to_list(length=None)
        for i in range(len(selections)):
            selections[i]["_id"] = str(selections[i]["_id"])
        return selections