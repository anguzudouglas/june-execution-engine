import os
import uuid
import shutil

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File


router = APIRouter()

UPLOAD_DIR = "storage/uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    upload_id = str(uuid.uuid4())

    upload_path = os.path.join(
        UPLOAD_DIR,
        upload_id
    )

    os.makedirs(
        upload_path,
        exist_ok=True
    )

    final_path = os.path.join(
        upload_path,
        file.filename
    )

    with open(final_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "success": True,
        "upload_id": upload_id,
        "filename": file.filename,
        "expires_in_minutes": 10
    }
