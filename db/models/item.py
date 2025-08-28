from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.config import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str | None] = mapped_column(Text(), nullable=True)
