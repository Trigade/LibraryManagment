from contextlib import asynccontextmanager
from fastapi import FastAPI
from controllers import book_controller,author_controller,category_controller,publisher_controller,member_controller,fine_controller,loan_controller
from database.db_service import DbService
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_service = DbService()
    db_service.initialize_database()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(book_controller.router)
app.include_router(author_controller.router)
app.include_router(category_controller.router)
app.include_router(publisher_controller.router)
app.include_router(member_controller.router)
app.include_router(fine_controller.router)
app.include_router(loan_controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000,reload=True)