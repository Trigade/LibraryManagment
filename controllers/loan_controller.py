from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.loan_response import LoanResponse, LoanCreate , LoanUpdate
from dtos.base_response import BaseResponse
from services.loans_service import LoansService
from repositories.loans_repository import LoansRepository
from repositories.fines_repository import FinesRepository
from services.fines_service import FinesService
from repositories.books_repository import BooksRepository
from services.books_service import BooksService

router = APIRouter(prefix="/loans",tags=["Loans"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()

def get_loan_service(conn = Depends(get_db_service)):
    loan_repository = LoansRepository()
    loan_service = LoansService(loan_repository, conn)
    return loan_service

def get_book_service(conn = Depends(get_db_service)):
    book_repository = BooksRepository()
    book_service = BooksService(book_repository, conn)
    return book_service

def get_fine_service(conn = Depends(get_db_service)):
    fine_repository = FinesRepository()
    fine_service = FinesService(fine_repository, conn)
    return fine_service

@router.get("/getloans/", response_model=BaseResponse[list[LoanResponse]])
def get_loans(loan_service= Depends(get_loan_service)):
    return loan_service.get_all()

@router.post("/addloan/")
def add_loan(loan: LoanCreate, loan_service= Depends(get_loan_service), book_service = Depends(get_book_service), fine_service = Depends(get_fine_service)):
    return loan_service.add_loan(loan,book_service,fine_service)

@router.patch("/{loan_id}", response_model=BaseResponse[int])
def update_loan(loan_id: int, loan: LoanUpdate, loan_service: LoansService = Depends(get_loan_service)):
    return loan_service.update_loan(loan_id, loan)

@router.delete("/{loan_id}",response_model=BaseResponse[int])
def delete_loan(loan_id:int,loan_service: LoansService = Depends(get_loan_service)):
    return loan_service.delete_loan(loan_id)

@router.get("/getloans/{loan_id}",response_model=BaseResponse[LoanResponse])
def get_loan_by_id(loan_id:int,loan_service: LoansService = Depends(get_loan_service)):
    return loan_service.get_by_id(loan_id)