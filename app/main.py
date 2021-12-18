from fastapi import FastAPI 

from app.apis.api_loader import api_router

def include_router(app):
    app.include_router(api_router)

def start_application() -> FastAPI:
    app = FastAPI(
        title="TSEU Sandbox", 
        openapi_url="/openapi.json", 
        docs_url="/docs", 
        description="FastAPI Idea Pool"
    )

    include_router(app)

    return app

app = start_application()

@app.get("/")
def root() -> dict:
    return {"Route": "Root"}