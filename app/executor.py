import os
import uuid
import shutil
import tempfile
import subprocess
import time
import base64

from app.validators import validate_code
from app.artifacts import collect_artifacts


def execute_code(code: str, timeout: int = 15, files=[]):

    validate_code(code)

    session_id = str(uuid.uuid4())

    temp_dir = tempfile.mkdtemp(prefix="exec_")

    try:

        for file in files:

            file_path = os.path.join(temp_dir, file.name)

            with open(file_path, "wb") as f:
                f.write(base64.b64decode(file.base64))

        wrapped_code = f"""
import matplotlib
matplotlib.use('Agg')

{code}
"""

        code_file = os.path.join(temp_dir, "main.py")

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

        execution_time = round(time.time() - start, 2)

        artifacts = collect_artifacts(temp_dir)

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "execution_time": execution_time,
            "artifacts": artifacts
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "error": {
                "type": "TimeoutError",
                "message": f"Execution exceeded {timeout} seconds"
            }
        }

    except Exception as e:

        return {
            "success": False,
            "error": {
                "type": type(e).__name__,
                "message": str(e)
            }
        }

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
