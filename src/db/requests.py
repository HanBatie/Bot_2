import asyncio

from src.db.models import User, Residental_Complex, Building, kpp_pass
from src.db.engine import async_session
from sqlalchemy import select, update, delete, Column, func, cast


async def db_add_user(tg_id, phone_number, name, Building_adress, R_C_id):
    async with async_session() as session:
        result = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not result:
            session.add(User(tg_id=tg_id, ph_number=str(phone_number), name=name, adress=Building_adress, R_C_id=R_C_id))
        else:
            await session.execute(update(User).values( ph_number=str(phone_number), name=name, adress=Building_adress).filter_by(tg_id=tg_id))
        await session.commit()


async def get_R_C(key):
    async with async_session() as session:
        query = select(Residental_Complex.name).where(Residental_Complex.key.in_([key]))
        queryy= select(Residental_Complex.id).where(Residental_Complex.key.in_([key]))
        result = await session.scalar(query)
        resultt = await session.scalar(queryy)

        if not result:
            return ['Ошибка: ключ подключения не распознан', 'Oshbka']
        else:
            return [str(result),int(resultt)]


async def db_add_kpp_pass(tg_id, auto_number, date_time, full_name):
    async with async_session() as session:
        session.add(kpp_pass(tg_id=tg_id, auto_number=auto_number, date_time=date_time, full_name=full_name))
        await session.commit()
