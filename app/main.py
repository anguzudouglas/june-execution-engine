from fastapi import FastAPI
from app.models import ExecuteRequest
from app.executor import execute_code

app = FastAPI(
    title="Python Execution API"
)


@app.get("/")
async def root():
    return {
        "status": "running"
    }


@app.post("/execute")
async def execute(request: ExecuteRequest):

    result = execute_code(
        code=request.code,
        timeout=request.timeout,
        files=request.files
    )

    return result
