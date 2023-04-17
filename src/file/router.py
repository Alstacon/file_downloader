from fastapi import APIRouter
from pydantic.types import UUID

from src.file.schemas import FileSchema
from src.file.service import create_file, get_files_list, get_file

router = APIRouter(
    prefix='/api/file',
    tags=['File']
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
async def get_file_page(uuid: UUID):
    """Получение файла по uuid"""
    file = await get_file(uuid)
    return {
        'status': 'ok',
        'data': file
    }
