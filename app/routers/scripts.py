from fastapi import APIRouter
from controller.script_controller import ScriptController
from schema.script_schema import ScriptGetRequest


script_controller = ScriptController()

router = APIRouter(
	prefix="/scripts",
    tags=["scripts"]
)

@router.get("/get_script/{order}",\
    description="detail 생성 및 저장")
async def get_script(order):
    script = await script_controller.get_script(order)
    if script:
        return { "result": "success", "script":script}
    else:
        return { "result": "fail" }