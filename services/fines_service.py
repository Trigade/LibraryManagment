import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.fine_response import FineResponse

class FinesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_fine(self,fine) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(fine,cursor)
                return BaseResponse(success=True,message="Ceza Eklendi",data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success= False,message=f"Ceza eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Beklenmedik bir hata oluştu {e}")

    def update(self,fine) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                row_count = self.__repository.update(fine, cursor)
                if row_count == 0:
                    return BaseResponse(success=False,message="Güncellenecek ceza bulunamadı.")
                return BaseResponse(success=True,message="Ceza başarıyla güncellendi.",data=row_count)
        except sq.Error as e:
            return BaseResponse(success= False,message=f"Ceza güncellenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Ceza güncellenirken beklenmedik bir hata oluştu {e}")

    def delete_fine(self,id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                row_count = self.__repository.delete(id,cursor)
                if row_count == 0:
                    return BaseResponse(succes=False,message="Silinecek ceza bulunamadı")
                return BaseResponse(success=True,message="Ceza silme işlemi başarılı.",data=row_count)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Ceza silinirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Ceza silinirken beklenmedik bir hata oluştu {e}")

    def get_by_id(self,id) -> BaseResponse[FineResponse]:
        try:
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Ceza bulunamadı.")
            fine = self.__repository.get_by_id(id,cursor)
            return BaseResponse(success=True,message="Ceza başarıyla getirildi",data=fine)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Ceza görüntülenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Ceza görüntülenirken beklenmedik bir hata oluştu {e}")
    
    def get_all(self) -> BaseResponse[list[FineResponse]]:
        try:
                cursor = self.__db.cursor()
                fine_list = self.__repository.get_all(cursor)
                return BaseResponse(success=True,message="Cezalar başarıyla getirildi", data=fine_list)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Cezalar listelenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Cezalar listelenirken bir hata oluştu {e}")