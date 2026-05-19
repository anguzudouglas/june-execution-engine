import os
import base64

from app.storage import save_artifact
from app.config import MAX_INLINE_SIZE_MB


def collect_artifacts(temp_dir, base_url):

    artifacts = []

    for file in os.listdir(temp_dir):

        path = os.path.join(temp_dir, file)

        if not os.path.isfile(path):
            continue

        size_mb = os.path.getsize(path) / (1024 * 1024)

        if size_mb <= MAX_INLINE_SIZE_MB:

            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()

            artifacts.append({
                "name": file,
                "delivery": "inline",
                "base64": encoded
            })

        else:

            artifact_id, final_path = save_artifact(path)

            artifacts.append({
                "name": file,
                "delivery": "url",
                "url": f"{base_url}/artifact/{artifact_id}/{file}"
            })

    return artifacts
