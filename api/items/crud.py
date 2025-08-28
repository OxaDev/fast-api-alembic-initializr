from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.items.schemas import ItemCreate
from db import models


async def create_item(db: AsyncSession, item_in: ItemCreate) -> models.Item:
    item = models.Item(name=item_in.name, description=item_in.description)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


async def get_item(db: AsyncSession, item_id: int) -> models.Item | None:
    res = await db.execute(select(models.Item).where(models.Item.id == item_id))
    return res.scalar_one_or_none()


async def list_items(
    db: AsyncSession, skip: int = 0, limit: int = 50
) -> list[models.Item]:
    res = await db.execute(select(models.Item).offset(skip).limit(limit))
    return list(res.scalars().all())


async def delete_item(db: AsyncSession, item_id: int) -> None:
    item = await get_item(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()
