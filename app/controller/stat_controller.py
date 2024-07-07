from models import mongodb
from bson import ObjectId
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import pytz

class StatController:
    async def ep1_start(self, name):
        current_time = datetime.now(ZoneInfo("Asia/Seoul"))
        result = await mongodb.db.stats.update_one(
            {"name": name},
            {
                "$set": {"created_at": current_time},
                "$setOnInsert": {"name":name, "clue_point":0, "detect_point":0, "detect_time":"00:00", "num_of_arrest": 0, "num_of_complete": 0}
            },
            upsert=True
        )
        return result
    
    async def update_stat(self, story_id, name, level, is_arrest):
        current_time = datetime.now(ZoneInfo("Asia/Seoul"))
        points = await mongodb.db.points.find({"story_id": story_id, "level": level, "name": name, "is_detect":1},{"_id": 0, "point": 1}).to_list(length=None)
        detect_point = 0
        if points:
            points_list = [doc["point"] for doc in points]
            detect_point = sum(points_list)
        
        clue_point = 0
        points_cursor = await mongodb.db.points.find({"story_id": story_id, "name": name, "level": level, "is_detect":0},{"_id": 0, "point": 1}).to_list(length=None)
        if points_cursor:
            points = [doc["point"] for doc in points_cursor]
            clue_point = sum(points)
        

        user_doc = await mongodb.db.stats.find_one({"name": name})
        if user_doc:
            # created_at과 현재 시간의 차이를 계산
            created_at = user_doc["created_at"]
            if created_at.tzinfo is None:
                created_at = pytz.utc.localize(created_at)
            time_difference = current_time - created_at

            existing_detect_time = user_doc['detect_time']
            hours, minutes = map(int, existing_detect_time.split(":"))
            existing_detect_timedelta = timedelta(hours=hours, minutes=minutes)

            # 새로 계산한 시간 차이와 기존 detect_time을 더함
            total_detect_timedelta = existing_detect_timedelta + time_difference

            # 시간 차이를 hh:mm 형식으로 변환
            total_seconds = total_detect_timedelta.total_seconds()
            hours, remainder = divmod(total_seconds, 3600)
            minutes = remainder // 60
            formatted_time = f"{int(hours):02d}:{int(minutes):02d}"

            # 기존 detect_point를 가져와 새롭게 계산한 detect_point와 더함
            existing_detect_point = user_doc['detect_point']
            total_detect_point = existing_detect_point + detect_point
            existing_clue_point = user_doc['clue_point']
            total_clue_point = existing_clue_point + clue_point
            # 문서 업데이트
            await mongodb.db.stats.update_one(
                {"name": name},
                {
                    "$set": {
                        "clue_point": total_clue_point,
                        "detect_point": total_detect_point,
                        "detect_time": formatted_time,
                        "num_of_arrest": user_doc['num_of_arrest'] + int(is_arrest),
                        "num_of_complete": user_doc['num_of_complete'] + 1
                    }
                }
            )
        return user_doc
    
    async def ep1_start(self, name):
        user_doc = await mongodb.db.stats.find_one({"name": name})
        user_doc['_id'] = str(user_doc['_id'])
        return user_doc