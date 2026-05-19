import os
import base64

from app.storage import save_artifact
from app.config import MAX_INLINE_SIZE_MB


SUPPORTED_EXTENSIONS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
    ".csv",
    ".xlsx",
    ".json",
    ".html",
    ".svg"
]


def collect_artifacts(temp_dir, base_url):

    artifacts = []

    for file in os.listdir(temp_dir):

        path = os.path.join(temp_dir, file)

        if not os.path.isfile(path):
            continue

        ext = os.path.splitext(file)[1].lower()

        if ext not in SUPPORTED_EXTENSIONS:
            continue

        size_mb = os.path.getsize(path) / (1024 * 1024)

        # small files -> inline base64
        if size_mb <= MAX_INLINE_SIZE_MB:

            with open(path, "rb") as f:
                encoded = base64.b64encode(
                    f.read()
                ).decode()

            artifacts.append({
                "name": file,
                "type": ext,
                "size_mb": round(size_mb, 2),
                "delivery": "inline",
                "base64": encoded
            })

        # large files -> temp URL
        else:

            artifact_id, filename = save_artifact(path)

            artifacts.append({
                "name": file,
                "type": ext,
                "size_mb": round(size_mb, 2),
                "delivery": "url",
                "url": f"{base_url}/artifact/{artifact_id}/{filename}"
            })

    return artifacts
