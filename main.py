from fastapi import FastAPI 

app = FastAPI(
    title="TSEU Sandbox", 
    openapi_url="/openapi.json", 
    docs_url="/docs", 
    description="FastAPI Idea Pool"
)

@app.get("/")
def root() -> dict:
    return {"Route": "Root"}