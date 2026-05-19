from pydantic import BaseModel

from typing import List
from typing import Optional


class UploadReference(BaseModel):

    upload_id: str

    filename: str


class ExecuteRequest(BaseModel):

    code: str

    timeout: Optional[int] = 30

    uploads: Optional[
        List[UploadReference]
    ] = []


class ArtifactResponse(BaseModel):

    artifact_id: str

    filename: str

    size: int

    url: str

    mime_type: str


class ErrorResponse(BaseModel):

    type: str

    message: str

    friendly_message: str
