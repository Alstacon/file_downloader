from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from src.models import File

file_pydentic = pydantic_model_creator(File)


class FileSchema(BaseModel):
    name: str
    type: str | None
