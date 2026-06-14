from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import crop, user

app = FastAPI(title="Agri Data Manager API")

# CORS 설정 (모바일 앱과 통신을 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시에는 도메인 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(crop.router, prefix="/crops", tags=["crops"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
