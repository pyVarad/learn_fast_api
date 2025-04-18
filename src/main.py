from fastapi import FastAPI, Header
from typing import Dict, Optional
from pydantic import BaseModel

app = FastAPI()


class CreateBook(BaseModel):
    title: str
    author: str


@app.get("/", status_code=200)
def healthz():
    return {"status": "working"}


@app.get("/greet/{name}", status_code=200)
async def greet(name: str) -> Dict:
    return {"greet": "Hello " + name}


@app.get("/sort", status_code=200)
async def sorted_content(sort_by: Optional[str] = "asc"):
    data = [1, 2, 3, 4, 5]
    resp = sorted(data) if sort_by == "asc" else sorted(data, reverse=True)
    return {"response": resp}


@app.post("/create_book", status_code=201)
async def create_book(book_data: CreateBook):
    title = book_data.title
    author = book_data.author

    return {"author": author, "title": title}


@app.get("/get_headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
