import sqlite3 as sq
from dtos.base_response import BaseResponse
from dtos.loan_response import LoanResponse

class LoansService:
    def __init__(self,repository,db):
        self.__repository = repository
        self.__db = db

    def add_loan(self,loan)->BaseResponse[int]:#kitap varmı ceza var mı bu kitap bu adamda var mı / karşılanırsa loan eklenir stock 1 düşer
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                lastrowid = self.__repository.add(loan,cursor)
                return BaseResponse(success=True,message="Borç başarıyla eklendi", data=lastrowid)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Borç eklenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Borç eklenirken beklenmedik bir hata oluştu {e}")
            
    def update(self,loan)->BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.update(loan, cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Güncellenecek borç bulunamadı")
                return BaseResponse(success=True,message="Borç başarıyla güncellendi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Borç güncellenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Borç güncellenirken beklenmedik bir hata oluştu {e}")

    def delete_loan(self,id) -> BaseResponse[int]:
        try:
            with self.__db as conn:
                cursor = conn.cursor()
                rowcount = self.__repository.delete(id,cursor)
                if rowcount == 0:
                    return BaseResponse(success=False,message="Silinecek borç bulunamadı")
                return BaseResponse(success=True,message="Borç başarıyla silindi", data=rowcount)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Borç silme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Borç silme işlemi sırasında beklenmedik bir hata oluştu {e}")
            
    def get_by_id(self,id) -> BaseResponse[LoanResponse]:
        try:    
            cursor = self.__db.cursor()
            if not self.__repository.get_by_id(id,cursor):
                return BaseResponse(success=False,message="Borç bulunamadı")
            loan = self.__repository.get_by_id(id,cursor)
            return BaseResponse(success=True,message="Borç başarıyla getirildi", data=loan)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Borç çekme işlemi sırasında veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Borç çekme işlemi sırasında beklenmedik bir hata oluştu {e}")
        
    def get_all(self) -> BaseResponse[list[LoanResponse]]:
        try:
            cursor = self.__db.cursor()
            loan_list = self.__repository.get_all(cursor)
            return BaseResponse(success=True,message="Borçlar başarıyla getirildi", data=loan_list)
        except sq.Error as e:
            return BaseResponse(success=False,message=f"Borçlar listelenirken veritabanı hatası oluştu {e}")
        except Exception as e:
            return BaseResponse(success=False,message=f"Borçlar listelenirken bir hata oluştu {e}")