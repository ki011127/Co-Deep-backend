from fastapi import APIRouter
from controller.clue_controller import ClueController
from schema.clue_schema import ClueCreateRequest

clue_controller = ClueController()

router = APIRouter(
	prefix="/clues",
    tags=["clues"]
)

@router.post("/get_clue",\
    description="단서 정보 반환")
async def get_clue(clue: ClueCreateRequest):
    clue = await clue_controller.get_clue(clue.id)
    if clue:
        return { "result": "success", "clue": clue}
    else:
        return { "result": "fail" }