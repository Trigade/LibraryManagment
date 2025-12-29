from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.author_response import AuthorResponse, AuthorCreate
from dtos.base_response import BaseResponse
from services.authors_service import AuthorsService
from repositories.authors_repository import AuthorsRepository

router = APIRouter(prefix="/authors",tags=["Authors"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()


def get_author_service(conn = Depends(get_db_service)):
    author_repository = AuthorsRepository()
    author_service = AuthorsService(author_repository, conn)
    return author_service

@router.get("/getauthors/", response_model=BaseResponse[list[AuthorResponse]])
def get_authors(author_service= Depends(get_author_service)):
    return author_service.get_all()

@router.post("/addauthor/")
def add_author(author: AuthorCreate, author_service= Depends(get_author_service)):
    return author_service.add_author(author)

