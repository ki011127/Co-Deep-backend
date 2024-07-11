from fastapi import APIRouter
from controller.rank_controller import RankController
from schema.rank_schema import StoryRankRequest

rank_controller = RankController()

router = APIRouter(
	prefix="/ranks",
    tags=["ranks"]
)

@router.post("/story_rank",\
    description="스토리 랭킹")
async def story_rank(stat: StoryRankRequest):
    rank = await rank_controller.story_rank(stat.story_id, stat.level)
    if rank:
        return { "result": "success", "rank": rank}
    else:
        return { "result": "fail" }
    
@router.get("/total_rank",\
    description="총합 점수 랭킹")
async def total_rank():
    rank = await rank_controller.total_rank()
    if rank:
        return { "result": "success", "rank": rank}
    else:
        return { "result": "fail" }