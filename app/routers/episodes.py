from fastapi import APIRouter
from controller.episode_controller import EpisodeController
from schema.episode_schema import EpisodeCreateRequest

episode_controller = EpisodeController()

router = APIRouter(
	prefix="/episodes",
    tags=["episodes"]
)

@router.post("/get_episodes",\
    description="story_id와 age에 맞는 episode 반환")
async def get_episodes(episode: EpisodeCreateRequest):
    print(episode.story_id)
    episodes = await episode_controller.get_episodes(episode.story_id, episode.age)
    if episodes:
        print(episode.story_id)
        return { "result": "success", "stories": episodes}
    else:
        return { "result": "fail" }