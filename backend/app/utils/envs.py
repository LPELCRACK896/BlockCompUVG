import os

def get_env_type():
    return os.getenv('APP_ENV', 'dev')