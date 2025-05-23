import os
from typing import Optional
from fastapi import FastAPI
from models import mongodb
from routers import users, stories, episodes, details, clues, selections, scripts, detects, points, stats, ranks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # FastAPI 모듈

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

app.include_router(users.router) # 다른 route파일들을 불러와 포함시킴
app.include_router(stories.router)
app.include_router(episodes.router)
app.include_router(details.router)
app.include_router(clues.router)
app.include_router(selections.router)
app.include_router(scripts.router)
app.include_router(detects.router)
app.include_router(points.router)
app.include_router(stats.router)
app.include_router(ranks.router)

@app.on_event("startup")
def on_app_start():
	mongodb.connect()

@app.on_event("shutdown")
async def on_app_shutdown():
	mongodb.close()

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }