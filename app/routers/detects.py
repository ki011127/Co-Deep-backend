from fastapi import APIRouter
from controller.detect_controller import DetectController
from schema.detect_schema import DetectChatRequest, AllDetectChatRequest

detect_controller = DetectController()

router = APIRouter(
	prefix="/chattings",
    tags=["chattings"]
)

@router.post("/create_chat",\
    description="채팅 생성")
async def create_chat(detect: DetectChatRequest):
    chatting = await detect_controller.create_chat(detect.story_id,detect.name, detect.level, detect.input, detect.created_at)
    if chatting:
        return {"result": "success", "chatting": chatting}
    else:
        return { "result": "fail" }
    
@router.post("/get_all_chat",\
    description="모든 채팅 가져오기")
async def get_all_chat(detect: AllDetectChatRequest):
    chattings = await detect_controller.get_all_chat(detect.story_id,detect.name, detect.level)
    if chattings:
        return {"result": "success", "chattings": chattings}
    else:
        return { "result": "fail" }
    
@router.post("/remove_all_chat",\
    description="모든 채팅 가져오기")
async def remove_all_chat(detect: AllDetectChatRequest):
    chattings = await detect_controller.remove_all_chat(detect.story_id,detect.name, detect.level)
    if chattings:
        return {"result": "success"}
    else:
        return { "result": "fail" }