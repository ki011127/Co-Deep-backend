from fastapi import APIRouter
from controller.detail_controller import DetailController
from schema.detail_schema import DetailCreateRequest
from schema.detail_schema import DetailGetRequest
from schema.detail_schema import WrongDetailRequest, GetAllDetailRequest

detail_controller = DetailController()

router = APIRouter(
	prefix="/details",
    tags=["details"]
)

# @router.post("/get_detail",\
#     description="detail 반환")
# async def get_detail(detail: DetailGetRequest):
#     details = await detail_controller.get_detail(detail.episode_id, detail.user_id)
#     if details:
#         return { "result": "success", "detail": details}
#     else:
#         return { "result": "fail" }

# @router.post("/wrong_detail",\
#     description="잘못된 선택지에 대한 detail 반환")
# async def wrong_detail(detail: WrongDetailRequest):
#     details = await detail_controller.wrong_detail(detail.episode_id, detail.user_id, detail.selection, detail.content, detail.created_at)
#     if details:
#         return { "result": "success", "detail": details}
#     else:
#         return { "result": "fail" }

# @router.post("/put_detail",\
#     description="detail 생성 및 저장")
# async def put_detail(detail: DetailCreateRequest):
#     detail = await detail_controller.put_detail(detail.episode_id, detail.user_id, detail.age, detail.story_name, detail.order, detail.created_at)
#     if detail:
#         return { "result": "success", "detail":detail}
#     else:
#         return { "result": "fail" }

@router.post("/get_all_detail",\
    description="detail 생성 및 저장")
async def get_all_detail(detail: GetAllDetailRequest):
    details = await detail_controller.get_all_detail(detail.episode_id)
    if details:
        return { "result": "success", "details":details}
    else:
        return { "result": "fail" }