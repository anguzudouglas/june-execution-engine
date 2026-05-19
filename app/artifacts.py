import os
import uuid
import shutil
import mimetypes


ARTIFACT_DIR = "storage/artifacts"


def collect_artifacts(
    temp_dir: str,
    base_url: str
):

    artifacts = []

    ignored = {
        "main.py"
    }

    for filename in os.listdir(
        temp_dir
    ):

        if filename in ignored:
            continue

        path = os.path.join(
            temp_dir,
            filename
        )

        if not os.path.isfile(path):
            continue

        artifact_id = str(
            uuid.uuid4()
        )

        target_dir = os.path.join(
            ARTIFACT_DIR,
            artifact_id
        )

        os.makedirs(
            target_dir,
            exist_ok=True
        )

        target_path = os.path.join(
            target_dir,
            filename
        )

        shutil.copy(
            path,
            target_path
        )

        mime_type, _ = mimetypes.guess_type(
            filename
        )

        size = os.path.getsize(
            target_path
        )

        artifacts.append({
            "artifact_id":
                artifact_id,

            "filename":
                filename,

            "size":
                size,

            "url":
                f"{base_url}/artifact/{artifact_id}/{filename}",

            "mime_type":
                mime_type or "application/octet-stream"
        })

    return artifacts
