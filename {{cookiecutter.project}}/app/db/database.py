# -*- coding: utf-8 -*-
import os

import humps
from doppler_env import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, declalred_attr

load_dotenv()
env = dict(os.environ)


class Model(DeclarativeBase):
    """
    Base for all ORM models.
    """

    @declalred_attr.directive
    def __tablename__(cls) -> str:
        return humps.decamalize(cls.__name__) + "s"

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )


engine = create_engine(env.str("DATABASE_URL"))
