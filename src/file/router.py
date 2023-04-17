from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic.types import UUID
from starlette.responses import FileResponse

from src.file.schemas import FileSchema
from src.file.service import create_file, get_files_list, check_token
from src.models import File

router = APIRouter(
    prefix='/api/file',
    tags=['File'],
)


@router.post('/')
async def upload_file(file_item: FileSchema):
    """Получение файла для загрузки в бд"""
    file_uuid = await create_file(file_item)
    return {
        'status': 'ok',
        'uuid': file_uuid
    }


@router.get('/')
async def get_file_list():
    """Список файлов"""
    file_list = await get_files_list()
    return {
        'status': 'ok',
        'data': file_list
    }


@router.get('/{uuid}')
async def get_file_page(uuid: UUID, token: Annotated[str, Depends(check_token)]):
    """Получение файла по uuid"""
    file_item = await File.get(uuid=uuid)
    if token:
        return FileResponse(file_item.path, media_type='application/octest-stream', filename=file_item.name)
    return FileResponse(file_item.blur_path, media_type='application/octest-stream', filename=file_item.name)
