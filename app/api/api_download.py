from typing import Any

from fastapi import APIRouter

from app.helpers.exception_handler import CustomException
from app.schemas.sche_base import DataResponse
from app.schemas.sche_download import DownloadFileRequest, DownloadFileResponse
from app.services.srv_download import DownloadService

router = APIRouter()


@router.post('', response_model=DataResponse[DownloadFileResponse])
def download(download_file_data: DownloadFileRequest) -> Any:
    try:
        url = DownloadService.download_entity_dataset(download_file_data.data_link, download_file_data.country_name,
                                                      download_file_data.administrative_division_code,
                                                      download_file_data.entity_type)
        return DataResponse().success_response(data={'url':url})
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
