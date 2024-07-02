from fastapi import APIRouter
from controller.detail_controller import DetailController
from schema.detail_schema import DetailCreateRequest
from schema.detail_schema import DetailGetRequest

detail_controller = DetailController()

router = APIRouter(
	prefix="/details",
    tags=["details"]
)

@router.post("/get_detail",\
    description="detail 반환")
async def get_detail(detail: DetailGetRequest):
    details = await detail_controller.get_detail(detail.episode_id, detail.user_id)
    if details:
        return { "result": "success", "detail": details}
    else:
        return { "result": "fail" }


@router.post("/put_detail",\
    description="detail 저장")
async def put_detail(detail: DetailCreateRequest):
    details = await detail_controller.put_detail(detail.episode_id, detail.content, detail.user_id, detail.created_at)
    if details:
        return { "result": "success"}
    else:
        return { "result": "fail" }