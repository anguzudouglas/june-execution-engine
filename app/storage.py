import os
import uuid
import shutil

BASE_DIR = "storage/artifacts"

os.makedirs(BASE_DIR, exist_ok=True)


def save_artifact(temp_file_path):

    artifact_id = str(uuid.uuid4())

    artifact_dir = os.path.join(BASE_DIR, artifact_id)

    os.makedirs(artifact_dir, exist_ok=True)

    filename = os.path.basename(temp_file_path)

    final_path = os.path.join(
        artifact_dir,
        filename
    )

    shutil.copy2(
        temp_file_path,
        final_path
    )

    return artifact_id, filename
