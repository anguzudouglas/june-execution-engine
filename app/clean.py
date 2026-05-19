import os
import shutil
from datetime import datetime, timedelta

BASE_DIR = "storage/artifacts"

EXPIRY_HOURS = 24


def cleanup_artifacts():

    now = datetime.utcnow()

    for artifact_id in os.listdir(BASE_DIR):

        path = os.path.join(BASE_DIR, artifact_id)

        created = datetime.utcfromtimestamp(
            os.path.getctime(path)
        )

        age = now - created

        if age > timedelta(hours=EXPIRY_HOURS):
            shutil.rmtree(path, ignore_errors=True)
