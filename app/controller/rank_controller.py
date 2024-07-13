from models import mongodb
from bson import ObjectId
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import pytz

class RankController:
    async def story_rank(self, story_id, name,level):
        result = await mongodb.db.stats.find(
            {"story_id": story_id, "level": level},
            {"_id": 0, "story_point": 1, "name": 1, "created_at":1}
        ).sort("story_point", -1).to_list(length=None)
        rank_list = []
        target = {}
        date = None
        # 결과 리스트에 is_target 필드를 추가 및 rank_list 생성
        for idx, doc in enumerate(result, start=1):
            doc["is_target"] = 1 if doc["name"] == name else 0
            rank_list.append(doc)

            # target 설정
            if doc["name"] == name:
                if not target or doc["created_at"] > date:
                    date = doc["created_at"]
                    target = {
                        "story_point": doc["story_point"],
                        "rank": idx
                    }

        return {"rank_list": rank_list, "target": target}
    
    async def total_rank(self, name):
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
                    "total_story_point": 1,
                    "created_at":1
                }
            }
        ]
        
        result = await mongodb.db.stats.aggregate(pipeline).to_list(length=None)
        rank_list = []
        target = {}

        # 결과 리스트에 is_target 필드를 추가 및 rank_list 생성
        for idx, doc in enumerate(result, start=1):
            doc["is_target"] = 1 if doc["name"] == name else 0
            rank_list.append(doc)

            # target 설정
            if doc["name"] == name:
                target = {
                    "total_story_point": doc["total_story_point"],
                    "rank": idx
                }

        return {"rank_list": rank_list, "target": target}