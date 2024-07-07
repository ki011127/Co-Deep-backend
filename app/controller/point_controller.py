from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo
from ai.point import Point
import os
import json

class PointController:
    async def detect_point(self, story_id, name, level, question, input):
        point_model = Point()
        content = "q : " + question + "\na : " + input
        res = point_model.point(content)
        if res == "0":
            count = await mongodb.db.points.count_documents({"story_id": story_id,"level": level,"name": name,"point": 0, "is_detect":1})
            if count == 4:
                return "failed"
        
        document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "point": int(res),
                "is_detect": 1
            }
        
        result = await mongodb.db.points.insert_one(document)
        points = await mongodb.db.points.find({"story_id": story_id, "level": level, "name": name, "is_detect":1},{"_id": 0, "point": 1}).to_list(length=None)
        total_point = -1
        if points:
            points_list = [doc["point"] for doc in points]
            total_point = sum(points_list)
        return total_point
    
    async def all_detect_point(self, story_id, name, level):
        points = await mongodb.db.points.find({"story_id": story_id, "level": level, "name": name, "is_detect":1},{"_id": 0, "point": 1}).to_list(length=None)
        total_point = -1
        if points:
            points_list = [doc["point"] for doc in points]
            total_point = sum(points_list)
        return total_point
    
    async def remove_point(self, story_id, name, level):
        result = await mongodb.db.points.delete_many({"story_id": story_id, "level": level, "name": name})
        return result
    
    async def add_clue_point(self, story_id, name, level, episode_id, is_hint, num_of_try, clue_order):
        clue = await mongodb.db.clues.find_one({"episode_id": episode_id, "order":clue_order})
        print(clue)
        clue['_id'] = str(clue['_id'])
        document = {}
        point = -1
        if is_hint == 0:
            if num_of_try == 1:
                document = {
                    "story_id": story_id,
                    "level": level,
                    "name": name,
                    "episode_id": episode_id,
                    "point": 3,
                    "is_detect": 0,
                    "clue": clue
                }
                point = 3
            else:
                document = {
                    "story_id": story_id,
                    "level": level,
                    "name": name,
                    "episode_id": episode_id,
                    "point": 2,
                    "is_detect": 0,
                    "clue": clue
                }
                point = 2
        elif is_hint == 1:
            document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "episode_id": episode_id,
                "point": 1,
                "is_detect": 0,
                "clue": clue
            }
            point = 1
        elif is_hint == 2:
            document = {
                "story_id": story_id,
                "level": level,
                "name": name,
                "episode_id": episode_id,
                "point": 0,
                "is_detect": 0,
                "clue": clue
            }
            point = 0
        result = await mongodb.db.points.insert_one(document)
        return point
    
    async def episode_clue_point(self, episode_id, name):
        total_sum = -1
        points_cursor = await mongodb.db.points.find({"episode_id": episode_id, "name": name},{"_id": 0, "point": 1}).to_list(length=None)
        points = [doc["point"] for doc in points_cursor]
        total_sum = sum(points)
        return total_sum
    
    async def all_clue_point(self, story_id, name, level):
        total_sum = -1
        points_cursor = await mongodb.db.points.find({"story_id": story_id, "name": name, "level": level, "is_detect": 0},{"_id": 0, "point": 1}).to_list(length=None)
        points = [doc["point"] for doc in points_cursor]
        total_sum = sum(points)
        return total_sum