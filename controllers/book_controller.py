from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.book_response import BookResponse, BookCreate , BookUpdate
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

@router.patch("/{book_id}", response_model=BaseResponse[int])
def update_book(book_id: int, book: BookUpdate, book_service: BooksService = Depends(get_book_service)):
    return book_service.update_book(book_id, book)

@router.delete("/{book_id}",response_model=BaseResponse[int])
def delete_book(book_id:int,book_service: BooksService = Depends(get_book_service)):
    return book_service.delete_book(book_id)

@router.get("/getbooks/{book_id}",response_model=BaseResponse[BookResponse])
def get_book_by_id(book_id:int,book_service: BooksService = Depends(get_book_service)):
    return book_service.get_by_id(book_id)