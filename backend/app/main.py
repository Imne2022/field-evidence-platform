from fastapi import FastAPI

from app.api import incidents as incidents_router
from app.core.config import settings


app = FastAPI(title=settings.app_name, version="0.1.0")

app.include_router(incidents_router.router, prefix="/api/v1")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}