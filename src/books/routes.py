from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .schemas import Books, UpdateBooks
from .models import Books as ResponseBookDTO
from src.db.main import get_session
from .service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession

books_router = APIRouter()
book_service = BookService()

@books_router.get("/", response_model=List[ResponseBookDTO], status_code=status.HTTP_200_OK)
async def get_all_books(session: AsyncSession = Depends(get_session)):
    return await book_service.get_all_books(session=session)

@books_router.get(
    "/{id}",
    summary="Get book by id",
    response_model=ResponseBookDTO,
    status_code=status.HTTP_200_OK,
)
async def get_book_by_id(id: str, session: AsyncSession=Depends(get_session)):
    book = await book_service.get_book(id, session=session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} is not found")

@books_router.post(
    "/",
    summary="Create new book",
    response_model=ResponseBookDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_a_book(book: Books, session: AsyncSession = Depends(get_session)):
    book = await book_service.add_new_book(book=book, session=session)
    return book


@books_router.patch(
    "/{id}",
    summary="Update an existing book",
    response_model=ResponseBookDTO,
    status_code=status.HTTP_201_CREATED,
)
async def update_a_book(id: str, book: UpdateBooks, session:AsyncSession=Depends(get_session)):
    book = await book_service.update_an_existing_book(id, book, session=session)
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
        )


@books_router.delete("/{id}")
async def delete_a_book(id: str, session:AsyncSession = Depends(get_session)):
    book = await book_service.delete_an_existing_book(id, session=session)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
        )