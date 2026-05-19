import os
import time
import shutil

from app.config import (
    UPLOAD_TTL_MINUTES,
    ARTIFACT_TTL_HOURS
)


def cleanup_directory(
    directory,
    ttl_seconds
):

    now = time.time()

    if not os.path.exists(directory):
        return

    for item in os.listdir(
        directory
    ):

        path = os.path.join(
            directory,
            item
        )

        if not os.path.isdir(path):
            continue

        created = os.path.getctime(
            path
        )

        age = now - created

        if age > ttl_seconds:

            shutil.rmtree(
                path,
                ignore_errors=True
            )


def cleanup_uploads():

    cleanup_directory(
        "storage/uploads",
        UPLOAD_TTL_MINUTES * 60
    )


def cleanup_artifacts():

    cleanup_directory(
        "storage/artifacts",
        ARTIFACT_TTL_HOURS * 3600
    )
