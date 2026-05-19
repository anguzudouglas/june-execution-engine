import os
import base64


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


def collect_artifacts(temp_dir):

    artifacts = []

    for file in os.listdir(temp_dir):

        path = os.path.join(temp_dir, file)

        if not os.path.isfile(path):
            continue

        ext = os.path.splitext(file)[1].lower()

        if ext not in SUPPORTED_EXTENSIONS:
            continue

        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        artifacts.append({
            "name": file,
            "type": ext,
            "base64": encoded
        })

    return artifacts
