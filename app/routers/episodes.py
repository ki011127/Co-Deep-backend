from fastapi import APIRouter
from controller.episode_controller import EpisodeController
from schema.episode_schema import EpisodeCreateRequest, EpisodeOrderRequest

episode_controller = EpisodeController()

router = APIRouter(
	prefix="/episodes",
    tags=["episodes"]
)

@router.post("/get_episodes",\
    description="story_id와 age에 맞는 episode 반환")
async def get_episodes(episode: EpisodeCreateRequest):
    print(episode.story_id)
    episodes = await episode_controller.get_episodes(episode.story_id, episode.level)
    if episodes:
        print(episode.story_id)
        return { "result": "success", "episodes": episodes}
    else:
        return { "result": "fail" }


@router.post("/episode_order",\
    description="story_id와 age에 맞는 episode 반환")
async def episode_order(episode: EpisodeOrderRequest):
    episodes = await episode_controller.episode_order(episode.story_id, episode.level, episode.order)
    if episodes:
        print(episode.story_id)
        return { "result": "success", "episodes": episodes}
    else:
        return { "result": "fail" }