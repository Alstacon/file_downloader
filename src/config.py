from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

DB_URL = f'asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

DB_MODELS = [
    'src.models',
    'aerich.models',
]

TORTOISE_ORM = {
    'connections': {'default': DB_URL},
    'apps': {
        'models': {
            'models': DB_MODELS,
            'default_connection': 'default',
        },
    },
}


API_TOKEN = os.environ.get('API_TOKEN')
