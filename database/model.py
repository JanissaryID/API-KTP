from sqlalchemy import Boolean, Column, String, Integer
from database.db_handler import Base


class KTPModel(Base):

    __tablename__ = "ktp"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    nik = Column(String, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    status = Column(Boolean, index=True, nullable=False, default=0)