from fastapi import FastAPI

app = FastAPI(title="Field Evidence Platform API", version="0.1.0")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "field-evidence-platform"}