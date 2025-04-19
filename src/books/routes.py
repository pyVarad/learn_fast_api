from fastapi import APIRouter, HTTPException, status
from typing import List
from .schemas import Books, UpdateBooks
from .books_data import books

books_router = APIRouter()


@books_router.get("/", response_model=List[Books], status_code=status.HTTP_200_OK)
async def get_all_books():
    return books


@books_router.get(
    "/{id}",
    summary="Get book by id",
    response_model=Books,
    status_code=status.HTTP_200_OK,
)
async def get_book_by_id(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
    )


@books_router.post(
    "/",
    summary="Create new book",
    response_model=Books,
    status_code=status.HTTP_201_CREATED,
)
async def create_a_book(book: Books):
    book = book.model_dump()
    books.books_routerend(book)

    return book


@books_router.patch(
    "/{id}",
    summary="Update an existing book",
    response_model=Books,
    status_code=status.HTTP_201_CREATED,
)
async def update_a_book(id: int, book: UpdateBooks):
    for book_info in books:
        if book_info["id"] == id:
            book_info["title"] = book.title
            book_info["author"] = book.author
            book_info["publisher"] = book.publisher
            book_info["page_count"] = book.page_count
            book_info["language"] = book.language

            return book_info

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
    )


@books_router.delete("/{id}")
async def delete_a_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
    return {}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
    )
