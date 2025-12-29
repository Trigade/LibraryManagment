import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.category_response import CategoryResponse

class CategoriesService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_category(self,category) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(category,cursor)
                return BaseResponse(success=True,message="Kategori başarıyla eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kategori eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Beklenmedik bir hata oluştu {e}")

    def update(self,category) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount=self.__repository.update(category, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek kategori bulunamadı")
                return BaseResponse(success=True,message="Kategori başarıyla güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Güncelleme sırasında bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Güncelleme sırasında beklenmedik bir hata oluştu {e}")
        
    def delete_category(self,id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount=self.__repository.delete(id,cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek kategori bulunamadı")
                return BaseResponse(success=True,message="Kategori başarıyla silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Silme işlemi sırasında beklenmedik bir hata oluştu {e}")

    def get_by_id(self,id)-> BaseResponse[CategoryResponse]:
        try:
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Kategori bulunamadı")
            return BaseResponse(success=True,message="Kategori başarıyla getirildi", data=self.__repository.get_by_id(id,cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kategori çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Kategori çekme işlemi sırasında beklenmedik bir hata oluştu {e}")
        
    def get_all(self) -> BaseResponse[list[CategoryResponse]]:
        try:
            cursor = self.__db.cursor()
            return BaseResponse(success=True,message="Kategoriler başarıyla listelendi", data=self.__repository.get_all(cursor))
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Kategoriler listelenirken bir veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Beklenmedik bir hata oluştu {e}")