from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


class Base(AsyncAttrs, DeclarativeBase): pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    tg_id = mapped_column(BigInteger)
    ph_number = mapped_column(String(20))
    adress: Mapped[str] = mapped_column(String(128))
    R_C_id: Mapped[int] = mapped_column()


class Residental_Complex(Base):
    __tablename__ = 'Residental_Complexes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    key: Mapped[str] = mapped_column()


class Building(Base):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(primary_key=True)
    adress: Mapped[int] = mapped_column()
    R_C: Mapped[int] = mapped_column(ForeignKey('Residental_Complexes.id'))


class kpp_pass(Base):
    __tablename__ = 'kpp_passes'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    auto_number: Mapped[str]  = mapped_column(String(10))
    date_time: Mapped[str] = mapped_column()
    full_name: Mapped[str] = mapped_column()

