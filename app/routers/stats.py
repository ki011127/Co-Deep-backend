from fastapi import APIRouter
from controller.stat_controller import StatController
from schema.stat_schema import StatCreateRequest

stat_controller = StatController()

router = APIRouter(
	prefix="/stats",
    tags=["stats"]
)

@router.post("/get_selections",\
    description="선택지 반환")
async def get_clue(select: StatCreateRequest):
    selections = await stat_controller.get_selections(select.selection_id)
    if selections:
        return { "result": "success", "selections": selections}
    else:
        return { "result": "fail" }