from fastapi import APIRouter
from controller.story_controller import StoryController
from schema.story_schema import StoryCreateRequest
from fastapi.encoders import jsonable_encoder

story_controller = StoryController()

router = APIRouter(
	prefix="/stories",
    tags=["stories"]
)

@router.get("/info/{age}",\
    description="페이지 접속 시 db내의 모든 스토리 정보 반환")
async def get_story(age):
    stories = await story_controller.get_story(age)
    if stories:
        return { "result": "success", "stories": stories}
    else:
        return { "result": "fail" }