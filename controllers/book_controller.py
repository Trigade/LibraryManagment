from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.book_response import BookResponse, BookCreate
from dtos.base_response import BaseResponse
from services.books_service import BooksService
from repositories.books_repository import BooksRepository

router = APIRouter(prefix="/books",tags=["Books"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()

def get_book_service(conn = Depends(get_db_service)):
    book_repository = BooksRepository()
    book_service = BooksService(book_repository, conn)
    return book_service

@router.get("/getbooks/", response_model=BaseResponse[list[BookResponse]])
def get_books(book_service= Depends(get_book_service)):
    return book_service.get_books()

@router.post("/addbook/")
def add_book(book: BookCreate, book_service= Depends(get_book_service)):
    return book_service.add_book(book)