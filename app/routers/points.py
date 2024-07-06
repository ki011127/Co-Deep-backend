from fastapi import APIRouter
from controller.point_controller import PointController
from schema.point_schema import DetectPointRequest, AllDetectPointRequest

detect_controller = PointController()

router = APIRouter(
	prefix="/points",
    tags=["points"]
)
    
@router.post("/detect_point",\
    description="유저 답변에 대한 점수")
async def detect_point(detect: DetectPointRequest):
    detect = await detect_controller.detect_point(detect.story_id,detect.name, detect.level, detect.question, detect.input)
    if detect:
        if detect == "failed":
            return {"result": "failure", "content" : "You failed to catch the culprit because you failed to infer. The incident falls into a mystery."}
        else:
            return {"result": "success", "point": detect}
    else:
        return { "result": "fail" }
    
@router.post("/all_detect_point",\
    description="추론 점수 합계")
async def all_detect_point(detect: AllDetectPointRequest):
    detect = await detect_controller.all_detect_point(detect.story_id,detect.name, detect.level)
    if detect:
        return {"result": "success", "total_point": detect}
    else:
        return { "result": "fail" }
    
@router.post("/remove_point",\
    description="추론 점수 삭제")
async def remove_point(detect: AllDetectPointRequest):
    detect = await detect_controller.remove_point(detect.story_id,detect.name, detect.level)
    if detect:
        return {"result": "success"}
    else:
        return { "result": "fail" }