from pydantic import BaseModel

class Books(BaseModel):
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
