from environs import Env
from dataclasses import dataclass


@dataclass
class Database:
    database_name: str
    user: str
    password: str
    host: str
    port: int


@dataclass
class DatabaseConfig:
    db: Database


def load_database_config(path: str | None = None) -> DatabaseConfig:
    env: Env = Env()
    env.read_env(path)
    return DatabaseConfig(db=Database(
        database_name=env('DATABASE'),
        user=env('USER'),
        password=env('PASSWORD'),
        host=env('HOST'),
        port=env('PORT')
    ))
