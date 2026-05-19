import os

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.models import ExecuteRequest
from app.executor import execute_code
from app.cleanup import cleanup_artifacts

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

    # cleanup expired artifacts
    cleanup_artifacts()

    result = execute_code(
        code=request.code,
        timeout=request.timeout,
        files=request.files
    )

    return result


@app.get("/artifact/{artifact_id}/{filename}")
async def get_artifact(
    artifact_id: str,
    filename: str
):

    path = os.path.join(
        "storage",
        "artifacts",
        artifact_id,
        filename
    )

    if not os.path.exists(path):

        return {
            "success": False,
            "status_code": 404,
            "error": {
                "message": "Artifact not found"
            }
        }

    return FileResponse(path)
