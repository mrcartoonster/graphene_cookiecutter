from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase
from enviorns import Env

env = Env()
env.read_env()


class Model(DeclarativeBase):
    """
    Base for all ORM models.
    """
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s"
        }
    )


engine = create_engine(env.str('DATABASE_URL'))