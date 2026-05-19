import os
import uuid
import shutil
import tempfile
import subprocess
import time

from app.artifacts import (
    collect_artifacts
)


def execute_code(
    code: str,
    timeout: int,
    uploads=[],
    base_url=""
):

    start = time.time()

    sandbox_id = str(
        uuid.uuid4()
    )

    temp_dir = tempfile.mkdtemp(
        prefix="exec_"
    )

    try:

        # restore uploads
        for upload in uploads:

            source_path = os.path.join(
                "storage",
                "uploads",
                upload["upload_id"],
                upload["filename"]
            )

            if os.path.exists(
                source_path
            ):

                target_path = os.path.join(
                    temp_dir,
                    upload["filename"]
                )

                shutil.copy(
                    source_path,
                    target_path
                )

        main_file = os.path.join(
            temp_dir,
            "main.py"
        )

        with open(
            main_file,
            "w"
        ) as f:

            f.write(code)

        process = subprocess.run(
            ["python", "main.py"],
            cwd=temp_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        stdout = process.stdout

        stderr = process.stderr

        success = (
            process.returncode == 0
        )

        artifacts = collect_artifacts(
            temp_dir,
            base_url
        )

        execution_time = round(
            time.time() - start,
            2
        )

        response = {
            "success":
                success,

            "status_code":
                200 if success else 400,

            "execution_time":
                execution_time,

            "sandbox_id":
                sandbox_id,

            "stdout":
                stdout,

            "stderr":
                stderr,

            "artifacts":
                artifacts,

            "error":
                None
        }

        if not success:

            error_line = stderr.splitlines()[-1] \
                if stderr else "Unknown error"

            response["error"] = {
                "type":
                    "RuntimeError",

                "message":
                    error_line,

                "friendly_message":
                    "The Python code raised an exception during execution."
            }

        return response

    except subprocess.TimeoutExpired:

        return {
            "success": False,

            "status_code": 408,

            "stdout": "",

            "stderr": "",

            "artifacts": [],

            "error": {
                "type":
                    "TimeoutError",

                "message":
                    f"Execution exceeded {timeout} seconds",

                "friendly_message":
                    "The execution took too long and was terminated."
            }
        }

    except Exception as e:

        return {
            "success": False,

            "status_code": 500,

            "stdout": "",

            "stderr": "",

            "artifacts": [],

            "error": {
                "type":
                    type(e).__name__,

                "message":
                    str(e),

                "friendly_message":
                    "An internal execution error occurred."
            }
        }

    finally:

        shutil.rmtree(
            temp_dir,
            ignore_errors=True
        )
