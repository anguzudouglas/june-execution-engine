import os
import uuid
import shutil


UPLOAD_DIR = "storage/uploads"


def save_upload(file):

    upload_id = str(
        uuid.uuid4()
    )

    target_dir = os.path.join(
        UPLOAD_DIR,
        upload_id
    )

    os.makedirs(
        target_dir,
        exist_ok=True
    )

    target_path = os.path.join(
        target_dir,
        file.filename
    )

    with open(
        target_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    size = os.path.getsize(
        target_path
    )

    return {
        "upload_id":
            upload_id,

        "filename":
            file.filename,

        "size":
            size
    }
