from src.file.schemas import FileSchema, file_pydentic
from src.models import File


async def create_file(file_item: FileSchema):
    new_file_item = await File.create(**file_item.dict())
    return new_file_item.uuid


async def get_files_list():
    file_list = File.all()
    return await file_pydentic.from_queryset(file_list)


async def get_file(uuid):
    file_item = File.get(uuid=uuid)
    return await file_pydentic.from_queryset_single(file_item)
