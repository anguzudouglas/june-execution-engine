from pydantic import BaseModel

from typing import List
from typing import Optional


class UploadedFile(BaseModel):

    upload_id: str

    filename: str


class InputFile(BaseModel):

    name: str

    base64: str


class ExecuteRequest(BaseModel):

    code: str

    timeout: Optional[int] = 15

    files: Optional[
        List[InputFile]
    ] = []

    uploads: Optional[
        List[UploadedFile]
    ] = []
