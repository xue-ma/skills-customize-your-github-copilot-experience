from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, Book] = {}
next_id = 1


@app.get("/books")
def list_books() -> dict[str, list[dict]]:
    return {"books": [{"id": book_id, **book.model_dump()} for book_id, book in books.items()]}


@app.get("/books/{book_id}")
def get_book(book_id: int) -> dict:
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": book_id, **books[book_id].model_dump()}


@app.post("/books", status_code=201)
def create_book(book: Book) -> dict:
    global next_id
    books[next_id] = book
    created_book = {"id": next_id, **book.model_dump()}
    next_id += 1
    return created_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book) -> dict:
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book
    return {"id": book_id, **book.model_dump()}


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": "Book deleted successfully"}
