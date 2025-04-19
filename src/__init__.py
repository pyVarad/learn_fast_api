from fastapi import FastAPI
from src.books.routes import books_router

version = "v1"

app = FastAPI(
    title="Bookly"
)
app.include_router(books_router, prefix=f"/api/{version}/book")