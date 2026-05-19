from fastapi import APIRouter
from fastapi import Request

from app.models import ExecuteRequest
from app.executor import execute_code
from app.cleanup import cleanup_artifacts


router = APIRouter()


@router.post("/execute")
async def execute(
    request: Request,
    payload: ExecuteRequest
):

    cleanup_artifacts()

    base_url = str(
        request.base_url
    ).rstrip("/")

    result = execute_code(
        code=payload.code,
        timeout=payload.timeout,
        files=payload.files,
        uploads=payload.uploads,
        base_url=base_url
    )

    return result
