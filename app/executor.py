import os
import shutil
import tempfile
import subprocess
import time
import base64

from app.validators import validate_code
from app.artifacts import collect_artifacts


def execute_code(code: str, timeout: int = 15, files=[],  base_url=""):

    temp_dir = tempfile.mkdtemp(prefix="exec_")

    try:

        validate_code(code)

        # restore uploaded files
        for file in files:

            file_path = os.path.join(
                temp_dir,
                file.name
            )

            with open(file_path, "wb") as f:
                f.write(
                    base64.b64decode(file.base64)
                )

        wrapped_code = f"""
import matplotlib
matplotlib.use('Agg')

{code}
"""

        code_file = os.path.join(
            temp_dir,
            "main.py"
        )

        with open(code_file, "w") as f:
            f.write(wrapped_code)

        start = time.time()

        result = subprocess.run(
            ["python", code_file],
            cwd=temp_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        execution_time = round(
            time.time() - start,
            2
        )

        # runtime failure
        if result.returncode != 0:

            error_message = "Runtime error"

            if result.stderr:

                lines = result.stderr.strip().splitlines()

                if lines:
                    error_message = lines[-1]

            return {
                "success": False,
                "status_code": 400,
                "execution_time": execution_time,

                "stdout": result.stdout,
                "stderr": result.stderr,

                "artifacts": [],

                "error": {
                    "type": "RuntimeError",
                    "message": error_message,
                    "friendly_message":
                        "The Python code raised an exception during execution."
                }
            }

        artifacts = collect_artifacts(
            temp_dir,
            base_url
        )

        return {
            "success": True,
            "status_code": 200,
            "execution_time": execution_time,

            "stdout": result.stdout,
            "stderr": result.stderr,

            "artifacts": artifacts,

            "error": None
        }

    except SyntaxError as e:

        return {
            "success": False,
            "status_code": 400,

            "stdout": "",
            "stderr": "",

            "artifacts": [],

            "error": {
                "type": "SyntaxError",
                "message": str(e),
                "line": e.lineno,
                "friendly_message":
                    f"Invalid Python syntax near line {e.lineno}."
            }
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "status_code": 408,

            "stdout": "",
            "stderr": "",

            "artifacts": [],

            "error": {
                "type": "TimeoutError",
                "message":
                    f"Execution exceeded {timeout} seconds.",

                "friendly_message":
                    "The Python code took too long to execute."
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
                "type": type(e).__name__,
                "message": str(e),

                "friendly_message":
                    "An internal execution error occurred."
            }
        }

    finally:
        shutil.rmtree(
            temp_dir,
            ignore_errors=True
        )
