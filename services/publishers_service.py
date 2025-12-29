import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.publisher_response import PublisherResponse

class PublishersService:
    def __init__(self, repository, db):
        self.__repository = repository
        self.__db = db

    def add_publisher(self, publisher) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(publisher, cursor)
                return BaseResponse(success=True,message="Yayıncı Başarıyla Eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yayıncı eklenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yayıncı eklenirken beklenmedik bir hata oluştu {e}")

    def update(self, publisher) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.update(publisher, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek yayıncı bulunamadı")
                return BaseResponse(success=True,message="Yayıncı Başarıyla Güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yayıncı güncellenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yayıncı güncellenirken beklenmedik bir hata oluştu {e}")

    def delete_publisher(self, id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount =self.__repository.delete(id, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek yayıncı bulunamadı")
                return BaseResponse(success=True,message="Yayıncı Başarıyla Silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yayıncı silinirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yayıncı silinirken beklenmedik bir hata oluştu {e}")

    def get_by_id(self, id) -> BaseResponse[PublisherResponse]:
        try:
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Yayıncı bulunamadı")
            return BaseResponse(success=True,message="Yayıncı başarıyla getirildi", data=self.__repository.get_by_id(id,cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yayıncı görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yayıncı görüntülenirken beklenmedik bir hata oluştu {e}")

    def get_all(self) -> BaseResponse[list[PublisherResponse]]:
        try:
            cursor = self.__db.cursor()
            return BaseResponse(success=True,message="Yayıncılar başarıyla listelendi", data=self.__repository.get_all(cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Yayıncılar listelenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Yayıncılar listelenirken beklenmedik bir hata oluştu {e}")
