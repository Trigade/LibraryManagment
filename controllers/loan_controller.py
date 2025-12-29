from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.loan_response import LoanResponse, LoanCreate
from dtos.base_response import BaseResponse
from services.loans_service import LoansService
from repositories.loans_repository import LoansRepository

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

@router.get("/getloans/", response_model=BaseResponse[list[LoanResponse]])
def get_loans(loan_service= Depends(get_loan_service)):
    return loan_service.get_all()

@router.post("/addloan/")
def add_loan(loan: LoanCreate, loan_service= Depends(get_loan_service)):
    return loan_service.add_loan(loan)