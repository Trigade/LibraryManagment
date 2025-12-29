from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.category_response import CategoryResponse, CategoryCreate
from dtos.base_response import BaseResponse
from services.categories_service import CategoriesService
from repositories.categories_repository import CategoriesRepository

router = APIRouter(prefix="/category",tags=["Category"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()

def get_category_service(conn = Depends(get_db_service)):
    category_repository = CategoriesRepository()
    category_service = CategoriesService(category_repository, conn)
    return category_service

@router.get("/getcategories/", response_model=BaseResponse[list[CategoryResponse]])
def get_categories(category_service= Depends(get_category_service)):

    return category_service.get_all()

@router.post("/addcategory/")
def add_category(category: CategoryCreate, category_service= Depends(get_category_service)):
    return category_service.add_category(category)