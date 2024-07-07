from fastapi import APIRouter
from controller.clue_controller import ClueController
from schema.clue_schema import ClueCheckRequest, UserClueRequest

clue_controller = ClueController()

router = APIRouter(
	prefix="/clues",
    tags=["clues"]
)

@router.post("/check_clue",\
    description="단서 정보 반환")
async def check_clue(clue: ClueCheckRequest):
    clue = await clue_controller.check_clue(clue.episode_id, clue.name, clue.num_of_try, clue.order)
    if clue:
        return clue
    else:
        return { "result": "fail" }
    

@router.post("/get_user_clues",\
    description="단서 정보 반환")
async def get_user_clues(clue: UserClueRequest):
    clue = await clue_controller.get_user_clues(clue.story_id, clue.name, clue.level)
    if clue:
        return {"result":"success", "clue_list":clue}
    else:
        return { "result": "fail" }