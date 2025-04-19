from fastapi import FastAPI, status, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import List


class SortBooksEnum(Enum):
    AUTHOR = "author"
    TITLE = "title"


app = FastAPI(title="Books API")


class Books(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class UpdateBooks(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


books = [
    {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publisher": "T. Egerton",
        "published_date": "1813-01-28",
        "page_count": 279,
        "language": "English",
    },
    {
        "id": 4,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons",
        "published_date": "1925-04-10",
        "page_count": 180,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Moby Dick",
        "author": "Herman Melville",
        "publisher": "Harper & Brothers",
        "published_date": "1851-10-18",
        "page_count": 635,
        "language": "English",
    },
    {
        "id": 6,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "publisher": "The Russian Messenger",
        "published_date": "1869-01-01",
        "page_count": 1225,
        "language": "Russian",
    },
    {
        "id": 7,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 277,
        "language": "English",
    },
    {
        "id": 8,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publisher": "George Allen & Unwin",
        "published_date": "1937-09-21",
        "page_count": 310,
        "language": "English",
    },
    {
        "id": 9,
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "publisher": "The Russian Messenger",
        "published_date": "1866-01-01",
        "page_count": 430,
        "language": "Russian",
    },
    {
        "id": 10,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperTorch",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese",
    },
]


@app.get("/books", response_model=List[Books], status_code=status.HTTP_200_OK)
async def get_all_books():
    return books


@app.get(
    "/book/{id}",
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


@app.post(
    "/book",
    summary="Create new book",
    response_model=Books,
    status_code=status.HTTP_201_CREATED,
)
async def create_a_book(book: Books):
    book = book.model_dump()
    books.append(book)

    return book


@app.patch(
    "/book/{id}",
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


@app.delete("/book/{id}")
async def delete_a_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
    return {}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book with {id} not found"
    )
