from models import mongodb
from bson import ObjectId
from datetime import datetime
from zoneinfo import ZoneInfo
from ai.wrong_selection import WrongSelection
import os
import json

class ScriptController:
    async def get_script(self, order):
        order = int(order)
        script = await mongodb.db.scripts.find({"order":order}).to_list(length=None)
        s = len(script)
        for i in range(s):
            script[i]["_id"] = str(script[i]["_id"])
            script[i]["num_of_scripts"] = 9
        return script
