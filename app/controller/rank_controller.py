from models import mongodb
from bson import ObjectId
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import pytz

class RankController:
    async def story_rank(self, story_id, level):
        result = await mongodb.db.stats.find(
            {"story_id": story_id, "level": level},
            {"_id": 0, "story_point": 1, "name": 1}
        ).sort("story_point", -1).to_list(length=None)

        return result
    
    async def total_rank(self):
        pipeline = [
            {
                "$group": {
                    "_id": "$name",
                    "total_story_point": {"$sum": "$story_point"}
                }
            },
            {
                "$sort": {
                    "total_story_point": -1
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "name": "$_id",
                    "total_story_point": 1
                }
            }
        ]
        
        result = await mongodb.db.stats.aggregate(pipeline).to_list(length=None)
        return result