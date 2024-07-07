from fastapi import APIRouter
from controller.point_controller import PointController
from schema.point_schema import DetectPointRequest, AllDetectPointRequest, AddCluePointRequest, EpisodePointRequest, CluePointRequest

point_controller = PointController()

router = APIRouter(
	prefix="/points",
    tags=["points"]
)
    
@router.post("/detect_point",\
    description="유저 답변에 대한 점수")
async def detect_point(point: DetectPointRequest):
    point = await point_controller.detect_point(point.story_id,point.name, point.level, point.question, point.input)
    if point or point!=-1:
        if point == "failed":
            return {"result": "failure", "content" : "You failed to catch the culprit because you failed to infer. The incident falls into a mystery."}
        else:
            return {"result": "success", "point": point}
    else:
        return { "result": "fail" }
    
@router.post("/all_detect_point",\
    description="추론 점수 합계")
async def all_detect_point(point: AllDetectPointRequest):
    point = await point_controller.all_detect_point(point.story_id,point.name, point.level)
    if point>=0:
        return {"result": "success", "total_point": point}
    else:
        return { "result": "fail" }
    
@router.post("/remove_point",\
    description="점수 삭제")
async def remove_point(point: AllDetectPointRequest):
    point = await point_controller.remove_point(point.story_id,point.name, point.level)
    if point:
        return {"result": "success"}
    else:
        return { "result": "fail" }
    
@router.post("/add_clue_point",\
    description="단서 점수 추가")
async def add_clue_point(point: AddCluePointRequest):
    point = await point_controller.add_clue_point(point.story_id,point.name, point.level, point.episode_id, point.is_hint, point.clue_order)
    if point>=0:
        return {"result": "success", "point": point}
    else:
        return { "result": "fail" }
    
@router.post("/episode_clue_point",\
    description="에피소드 단서 점수 합계")
async def episode_clue_point(point: EpisodePointRequest):
    point = await point_controller.episode_clue_point(point.episode_id, point.name)
    if point>=0:
        return {"result": "success", "point": point}
    else:
        return { "result": "fail" }
    
@router.post("/all_clue_point",\
    description="단서 점수 합계")
async def all_clue_point(point: CluePointRequest):
    point = await point_controller.all_clue_point(point.story_id,point.name, point.level)
    if point>=0:
        return {"result": "success", "point": point}
    else:
        return { "result": "fail" }