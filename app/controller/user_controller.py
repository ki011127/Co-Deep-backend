from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo

class UserController:    
    async def create_user(self, name, age):
        # existing_user = await mongodb.engine.find_one(Users, Users.uuid == uuid)
        existing_user = await mongodb.db.users.find_one({"name": name })
        if existing_user:
            # 기존 사용자가 있으면, 해당 사용자의 ID를 반환
            print(existing_user)
            return existing_user
        else:
            # 사용자가 없으면, 새로운 사용자를 추가
            ver = 0
            if age < 14:
                ver = 1
            elif age < 17:
                ver = 2
            else:
                ver = 3
            new_user = await mongodb.db.users.insert_one({"name": name, "age": ver})
            find_user = await mongodb.db.users.find_one({"name": name })
            print(find_user)
            return find_user