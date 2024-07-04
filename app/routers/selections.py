from fastapi import APIRouter
from controller.selection_controller import SelectionController
from schema.selection_schema import SelectionCreateRequest

selection_controller = SelectionController()

router = APIRouter(
	prefix="/selections",
    tags=["selections"]
)

@router.post("/get_selections",\
    description="선택지 반환")
async def get_clue(select: SelectionCreateRequest):
    selections = await selection_controller.get_selections(select.selection_id)
    if selections:
        return { "result": "success", "selections": selections}
    else:
        return { "result": "fail" }