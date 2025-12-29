from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.fine_response import FineResponse, FineCreate
from dtos.base_response import BaseResponse
from services.fines_service import FinesService
from repositories.fines_repository import FinesRepository

router = APIRouter(prefix="/fines",tags=["Fines"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()

def get_fine_service(conn = Depends(get_db_service)):
    fine_repository = FinesRepository()
    fine_service = FinesService(fine_repository, conn)
    return fine_service

@router.get("/getfines/", response_model=BaseResponse[list[FineResponse]])
def get_fines(fine_service= Depends(get_fine_service)):
    return fine_service.get_fines()

@router.post("/addfine/")
def add_fine(fine: FineCreate, fine_service= Depends(get_fine_service)):
    return fine_service.add_fine(fine)