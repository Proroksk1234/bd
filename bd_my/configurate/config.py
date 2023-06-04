import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-12]
config = Config(f'{root_dir}/secret_files/.env')

"""
Настройки запуска fastapi
"""

API_PREFIX = config('API_PREFIX', default='')
VERSION = '0.3.0'
DEBUG = config('DEBUG', cast=bool, default=False)
PROJECT_NAME = config('PROJECT_NAME', default='CRM')
OPENAPI_URL = config('OPENAPI_URL', default='/openapi.json')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings, default='')
ALLOWED_METHODS = config('ALLOWED_METHODS', cast=CommaSeparatedStrings, default=['*'])
ALLOWED_HEADERS = config('ALLOWED_HEADERS', cast=CommaSeparatedStrings, default=['*'])
ORIGINS = config('ORIGINS', default='*').split(',')
ALLOWED_CREDENTIALS = config('ALLOWED_HEADERS', default=True)

"""
Конфигурация настроек подключения к базе данных
"""
DATABASE_PORT = config('DATABASE_PORT', default=0)
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', default='')
POSTGRES_USER = config('POSTGRES_USER', default='')
POSTGRES_DB = config('POSTGRES_DB', default='')
POSTGRES_HOST = config('POSTGRES_HOST', default='')
POSTGRES_HOSTNAME = config('POSTGRES_HOSTNAME', default='')
SQLALCHEMY_DATABASE_URL = f"{POSTGRES_HOST}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{DATABASE_PORT}/{POSTGRES_DB}"
