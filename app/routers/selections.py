from fastapi import APIRouter
from controller.episode_controller import EpisodeController
from schema.episode_schema import EpisodeCreateRequest

episode_controller = EpisodeController()

router = APIRouter(
	prefix="/selections",
    tags=["selections"]
)

@router.post("/get_clue",\
    description="단서 정보 반환")
async def get_clue(clue: EpisodeCreateRequest):
    print(clue.story_id)
    episodes = await episode_controller.get_clue(clue.clue_id)
    if episodes:
        print(clue.story_id)
        return { "result": "success", "stories": episodes}
    else:
        return { "result": "fail" }