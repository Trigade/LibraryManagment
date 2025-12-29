from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.publisher_response import PublisherResponse, PublisherCreate
from dtos.base_response import BaseResponse
from services.publishers_service import PublishersService
from repositories.publishers_repository import PublishersRepository

router = APIRouter(prefix="/publishers",tags=["Publishers"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()

def get_publisher_service(conn = Depends(get_db_service)):
    publisher_repository = PublishersRepository()
    publisher_service = PublishersService(publisher_repository, conn)
    return publisher_service


@router.get("/getpublishers/", response_model=BaseResponse[list[PublisherResponse]])
def get_publishers(publisher_service= Depends(get_publisher_service)):
    return publisher_service.get_all()

@router.post("/addpublisher/")
def add_publisher(publisher: PublisherCreate, publisher_service= Depends(get_publisher_service)):
    return publisher_service.add_publisher(publisher)