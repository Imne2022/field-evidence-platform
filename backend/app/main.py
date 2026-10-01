from fastapi import FastAPI

# Import existing routers
from app.api.incidents import router as incidents_router
# Import the new tasks router (based on Step 22 path)
from app.api.tasks import router as tasks_router 

app = FastAPI(
    title="Field Evidence Platform",
    version="0.1.0",
)

# Register incidents router
app.include_router(
    incidents_router,
    prefix="/api/v1",
)

# Register tasks router
app.include_router(
    tasks_router,
    prefix="/api/v1",
)

# (Keep your existing /health endpoint and any other configuration below)