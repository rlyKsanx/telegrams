# from datetime import datetime
# from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)

from app.config import settings


engine = create_async_engine(url=settings.DATABASE_URL, echo=False)
session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # created_at: Mapped[datetime] = mapped_column(
    #     default="",
    #     server_default=func.now(),
    # )
    # updated_at: Mapped[datetime] = mapped_column(
    #     default="",
    #     server_default=func.now(),
    #     onupdate=func.now(),
    # )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
