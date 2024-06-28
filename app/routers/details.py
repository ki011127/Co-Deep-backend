from fastapi import APIRouter
from controller.detail_controller import DetailController
from schema.episode_schema import EpisodeCreateRequest

detail_controller = DetailController()

router = APIRouter(
	prefix="/details",
    tags=["details"]
)

@router.post("/get_detail",\
    description="단서 정보 반환")
async def get_detail(clue: EpisodeCreateRequest):
    print(clue.story_id)
    detail = await detail_controller.get_detail(clue.clue_id)
    if detail:
        print(clue.story_id)
        return { "result": "success", "detail": detail}
    else:
        return { "result": "fail" }


@router.post("/put_detail",\
    description="단서 정보 반환")
async def get_detail(clue: EpisodeCreateRequest):
    print(clue.story_id)
    detail = await detail_controller.get_detail(clue.clue_id)
    if detail:
        print(clue.story_id)
        return { "result": "success", "detail": detail}
    else:
        return { "result": "fail" }