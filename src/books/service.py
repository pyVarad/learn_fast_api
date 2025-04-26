from sqlmodel import select, desc
from typing import List
import uuid
from src.books.models import Books
from src.books.schemas import UpdateBooks, Books as NewBook
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime


class BookService:
    async def get_all_books(self, session: AsyncSession) -> List[NewBook]:
        statement = select(Books).order_by(desc(Books.created_at))
        result = await session.exec(statement=statement)
        return result.all()

    async def get_book(self, uid: str, session: AsyncSession) -> NewBook:
        statement = select(Books).where(Books.uid == uid)
        result = await session.exec(statement=statement)
        book = result.first()
        return book if book else None

    async def add_new_book(self, book: NewBook, session: AsyncSession) -> Books:
        book_info = book.model_dump()
        new_book = Books(**book_info)
        new_book.published_date = datetime.strptime(book_info["published_date"], "%Y-%m-%d")
        session.add(new_book)
        await session.commit()
        return new_book

    async def update_an_existing_book(
        self, uid: str, update_book: UpdateBooks, session: AsyncSession
    ) -> NewBook:
        book = await self.get_book(uid, session=session)
        if book:
            book_data = update_book.model_dump()
            for k, v in book_data.items():
                setattr(book, k, v)
            await session.commit()
            return book
        return None

    async def delete_an_existing_book(self, uid: str, session: AsyncSession) -> NewBook:
        book = await self.get_book(uid, session=session)
        if book:
            await session.delete(book)
            await session.commit()
            return {}
        return None
