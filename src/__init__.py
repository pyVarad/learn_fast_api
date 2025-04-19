from fastapi import FastAPI
from src.books.routes import books_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(r"Server Starting...")
    await init_db()
    yield
    print(r"Server Stopped...")

version = "v1"
app = FastAPI(
    title="Bookly",
    lifespan=life_span
)
app.include_router(books_router, prefix=f"/api/{version}/book")