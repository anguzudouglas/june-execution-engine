import os

from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()


@router.get(
    "/artifact/{artifact_id}/{filename}"
)
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
