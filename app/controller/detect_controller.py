from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo
from ai.detect import Detect
from ai.point import Point
import os
import json

class DetectController:
    async def create_chat(self, story_id, name, level, input, created_at):
        detect_model = Detect()
        result = await mongodb.db.chattings.find({"story_id":story_id, "name":name, "level":level}).sort("created_at", 1).to_list(length=None)
        res = ""
        document = {}
        if result:
            print("append")
            document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "created_at": created_at,
                "is_init": 0,
                "is_user": 1,
                "chat": input
            }
            await mongodb.db.chattings.insert_one(document)
            result.append(document)
            print(result)
            res = await detect_model.chatting(result)
            document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "created_at": created_at,
                "is_init": 0,
                "is_user": 0,
                "chat": res
            }
        else:
            print("init")
            res = await detect_model.init_model()
            document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "created_at": created_at,
                "is_init": 1,
                "is_user": 0,
                "chat": res
            }
        print(res)
        
        result = await mongodb.db.chattings.insert_one(document)
        if "-the end-" in res:
            return {
                "is_end": 1,
                "content": res
            }
        return {
            "is_end": 0,
            "content": res
        }
    
    async def get_all_chat(self, story_id, name, level):
        result = await mongodb.db.chattings.find({"story_id":story_id, "name":name, "level":level},{"_id":0, "is_user":1, "chat":1}).sort("created_at", 1).to_list(length=None)
        print(result)
        return result
    
    async def remove_all_chat(self, story_id, name, level):
        result = await mongodb.db.chattings.delete_many({"story_id": story_id, "level": level, "name": name})
        return result