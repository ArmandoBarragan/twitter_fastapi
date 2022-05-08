import os


DEBUG = os.getenv('DEBUG', default=False)

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_PORT = os.getenv('DATABASE_PORT')
