from fastapi import APIRouter, Depends
from database.db_service import DbService
from dtos.member_response import MemberResponse, MemberCreate
from dtos.base_response import BaseResponse
from services.members_service import MembersService
from repositories.members_repository import MembersRepository

router = APIRouter(prefix="/members",tags=["Members"])

def get_db_service():
    db_service = DbService()
    db = db_service.get_db_connection()
    try:
        yield db
    finally:
        db.close()


def get_member_service(conn = Depends(get_db_service)):
    member_repository = MembersRepository()
    member_service = MembersService(member_repository, conn)
    return member_service


@router.get("/getmembers/", response_model=BaseResponse[list[MemberResponse]])
def get_member(member_service= Depends(get_member_service)):
    return member_service.get_all()

@router.post("/addmember/")
def add_member(member: MemberCreate, member_service= Depends(get_member_service)):
    return member_service.add_member(member)