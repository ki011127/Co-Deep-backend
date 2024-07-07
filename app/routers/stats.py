from fastapi import APIRouter
from controller.stat_controller import StatController
from schema.stat_schema import StatCreateRequest, UpdateStatRequest

stat_controller = StatController()

router = APIRouter(
	prefix="/stats",
    tags=["stats"]
)

@router.post("/ep1_start",\
    description="선택지 반환")
async def ep1_start(stat: StatCreateRequest):
    stat = await stat_controller.ep1_start(stat.name)
    if stat:
        return { "result": "success"}
    else:
        return { "result": "fail" }
    
@router.post("/update_stat",\
    description="추론 페이지 끝나면 stat update를 위해 호출")
async def update_stat(stat: UpdateStatRequest):
    stat = await stat_controller.update_stat(stat.story_id, stat.name, stat.level, stat.is_arrest)
    if stat:
        return { "result": "success"}
    else:
        return { "result": "fail" }
    
@router.get("/get_stat/{name}",\
    description="추론 페이지 끝나면 stat update를 위해 호출")
async def update_stat(name):
    stat = await stat_controller.update_stat(name)
    if stat:
        return { "result": "success", "stat":stat}
    else:
        return { "result": "fail" }