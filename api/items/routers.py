from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.items import crud, schemas
from db.config import get_session

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=schemas.ItemRead, status_code=201)
async def create_item(
    item: schemas.ItemCreate, db: AsyncSession = Depends(get_session)
):
    return await crud.create_item(db, item)


@router.get("/{item_id}", response_model=schemas.ItemRead)
async def read_item(item_id: int, db: AsyncSession = Depends(get_session)):
    obj = await crud.get_item(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return obj


@router.get("/", response_model=list[schemas.ItemRead])
async def list_all(
    skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_session)
):
    return await crud.list_items(db, skip=skip, limit=limit)


@router.delete("/{item_id}", response_model=None, status_code=204)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_session)):
    return await crud.delete_item(db, item_id)
