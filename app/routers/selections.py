from fastapi import APIRouter
from controller.selection_controller import SelectionController
from schema.episode_schema import EpisodeCreateRequest

selection_controller = SelectionController()

router = APIRouter(
	prefix="/selections",
    tags=["selections"]
)

@router.post("/get_selection",\
    description="선택지 반환")
async def get_clue(clue: EpisodeCreateRequest):
    print(clue.story_id)
    selections = await selection_controller.get_selection(clue.clue_id)
    if selections:
        print(clue.story_id)
        return { "result": "success", "selections": selections}
    else:
        return { "result": "fail" }