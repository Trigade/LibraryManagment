import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.member_response import MemberResponse

class MembersService:
    def __init__(self, repository,db):
        self.__repository = repository
        self.__db = db

    def add_member(self, member) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(member,cursor)
                return BaseResponse(success=True,message="Üye başarıyla eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Üye eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Üye eklenirken beklenmedik bir hata oluştu {e}")

    def update_member(self, member)-> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.update(member, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek üye bulunamadı")
                return BaseResponse(success=True,message="Üye başarıyla güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Üye güncellenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Üye güncellenirken beklenmedik bir hata oluştu {e}")


    def delete_member(self, id)-> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.delete(id,cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek üye bulunamadı")
                return BaseResponse(success=True,message="Üye başarıyla silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Üye silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Üye silme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_by_id(self, id)-> BaseResponse[MemberResponse]:
        try:    
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Üye bulunamadı")
            book = self.__repository.get_by_id(id,cursor)
            return BaseResponse(success=True,message="Üye başarıyla getirildi", data=book)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Üye çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Üye çekme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_all(self)-> BaseResponse[list[MemberResponse]]:
        try:
            cursor = self.__db.cursor()
            book_list = self.__repository.get_all(cursor)
            return BaseResponse(success=True,message="Üyeler başarıyla getirildi", data=book_list)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Üyeler listelenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Üyeler listelenirken bir hata oluştu {e}")