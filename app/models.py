from pydantic import BaseModel
from typing import Optional, List


class ArtifactOptions(BaseModel):
    capture_plots: bool = True
    capture_files: bool = True
    return_base64: bool = True


class FileInput(BaseModel):
    name: str
    base64: str


class ExecuteRequest(BaseModel):
    code: str
    session_id: Optional[str] = None
    timeout: Optional[int] = 15
    files: Optional[List[FileInput]] = []
    artifacts: Optional[ArtifactOptions] = ArtifactOptions()
