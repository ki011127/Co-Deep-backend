from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class DetailController:
    async def get_detail(self, episode_id, user_id):
        details = await mongodb.db.details.find({"episode_id": episode_id, "user_id": user_id},
            {"_id": 0, "episode_id":1,"content": 1, "user_id": 1, "created_at": 1}
        ).to_list(length=None)
        print(details)
        return details
    
    async def put_detail(self, episode_id, content, user_id, created_at):
        detail = {
            "episode_id": episode_id,
            "content": content,
            "user_id": user_id,
            "created_at": created_at,
        }
        details = await mongodb.db.details.insert_one(detail)
        return details