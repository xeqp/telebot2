from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from TZ1_TZ2.database.models import User


async def create_user(db: AsyncSession, user_id: str, thread_id: str = None, moral_values: list = []):
    new_user = User(telegram_user_id=user_id, thread_id=thread_id, values=moral_values)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_telegram_id(db: AsyncSession, telegram_user_id: str):
    stmt = select(User).where(User.telegram_user_id == telegram_user_id)
    result = await db.execute(stmt)
    return result.scalars().first()


async def update_user_values(db: AsyncSession, user_telegram_id: str, new_values: list):
    user = await get_user_by_telegram_id(db, user_telegram_id)

    if user:
        updated_values = list(set(user.values + new_values))
        stmt = select(User).where(User.telegram_user_id == user_telegram_id).values(values=updated_values)
        await db.execute(stmt)
        await db.commit()
    else:
        print("User not found.")
