from pydantic import BaseModel


class DownloadFileRequest(BaseModel):
    data_link: str
    entity_type: str
    country_name: str
    administrative_division_code: str


class DownloadFileResponse(BaseModel):
    url: str
