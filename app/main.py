from fastapi.responses import FileResponse
import os

ARTIFACT_DIR = "storage/artifacts"


@app.get("/artifact/{artifact_id}/{filename}")
async def get_artifact(artifact_id: str, filename: str):

    path = os.path.join(
        ARTIFACT_DIR,
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
