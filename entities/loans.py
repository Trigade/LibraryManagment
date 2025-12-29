class Loans:
    def __init__(self,loan_date,due_date,return_date,member_id,book_id,id = None):
        self.id = id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date
        self.member_id =member_id
        self.book_id = book_id