import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.book_response import BookResponse

class BooksService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db
    def add_book(self,book) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(book,cursor)
                return BaseResponse(success=True,message="Kitap başarıyla eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kitap eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Beklenmedik bir hata oluştu {e}")

    def update_book(self,book) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.update(book, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek kitap bulunamadı")
                return BaseResponse(success=True,message="Kitap başarıyla güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kitap güncellenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Kitap güncellenirken beklenmedik bir hata oluştu {e}")

    def delete_book(self,id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.delete(id,cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek kitap bulunamadı")
                return BaseResponse(success=True,message="Kitap başarıyla silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_book(self,id) -> BaseResponse[BookResponse]:
        try:    
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Kitap bulunamadı")
            book = self.__repository.get_by_id(id,cursor)
            return BaseResponse(success=True,message="Kitap başarıyla getirildi", data=book)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Veri çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Veri çekme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_books(self) -> BaseResponse[list[BookResponse]]:
        try:
            cursor = self.__db.cursor()
            book_list = self.__repository.get_all(cursor)
            return BaseResponse(success=True,message="Kitaplar başarıyla getirildi", data=book_list)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kitaplar listelenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Kitaplar listelenirken bir hata oluştu {e}")