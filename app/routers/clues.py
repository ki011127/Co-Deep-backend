from fastapi import APIRouter
from controller.clue_controller import ClueController
from schema.clue_schema import ClueCheckRequest

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