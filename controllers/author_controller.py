from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.author_response import AuthorResponse, AuthorCreate , AuthorUpdate
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

@router.patch("/{author_id}", response_model=BaseResponse[int])
def update_author(author_id: int, author: AuthorUpdate, author_service: AuthorsService = Depends(get_author_service)):
    return author_service.update_author(author_id, author)

@router.delete("/{author_id}",response_model=BaseResponse[int])
def delete_author(author_id:int,author_service: AuthorsService = Depends(get_author_service)):
    return author_service.delete_author(author_id)

@router.get("/getauthors/{author_id}",response_model=BaseResponse[AuthorResponse])
def get_author_by_id(author_id:int,author_service: AuthorsService = Depends(get_author_service)):
    return author_service.get_by_id(author_id)