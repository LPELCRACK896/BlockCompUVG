from utils.envs import get_env_type
from config.config import Settings
from config.mongo import Mongo

from typing import Tuple


def setup_config() -> Tuple[Settings, Mongo]:
    env_type = get_env_type()
    settings = Settings(env_type)
    settings.setup_config()
    mongo = Mongo(settings.MONGO_URI)

    return settings, mongo



