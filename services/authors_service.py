import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.author_response import AuthorResponse

class AuthorsService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_author(self,author) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(author, cursor)
                return BaseResponse(success=True,message="Yazar başarıyla eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yazar eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yazar eklenirken beklenmedik bir hata oluştu {e}")
    
    def update_author(self,author)-> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.update(author, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek yazar bulunamadı")
                return BaseResponse(success=True,message="Yazar başarıyla güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Güncelleme sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Güncelleme sırasında beklenmeyen bir hata oluştu {e}")

    def delete_author(self,id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.delete(id,cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek yazar bulunamadı")
                return BaseResponse(success=True,message="Yazar başarıyla silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında beklenmeyen bir hata oluştu {e}")

    def get_by_id(self,id) -> BaseResponse[AuthorResponse]:
        try:
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Yazar bulunamadı")
            return BaseResponse(success=True,message="Yazar başarıyla getirildi", data=self.__repository.get_by_id(id,cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Veri çekilirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Veri çekilirken beklenmedik bir hata oluştu {e}")
        
    def get_all(self) -> BaseResponse[list[AuthorResponse]]:
        try:
            cursor = self.__db.cursor()
            return BaseResponse(success=True,message="Yazarlar başarıyla listelendi", data=self.__repository.get_all(cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yazarlar listelenirken veritabanı hatası: {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Hata: {e}")