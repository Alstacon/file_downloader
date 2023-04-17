from typing import Union

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.file.router import router as file_router

from src.config import DB_URL, DB_MODELS

app = FastAPI()

register_tortoise(
    app,
    db_url=DB_URL,
    modules={'models': DB_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(file_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
