from sqlalchemy.orm import Mapped

from app.db.base import Base


class Telegram(Base):
    id_user: Mapped[str]
