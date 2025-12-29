class Fines:
    def __init__(self,amount,payment_status,loan_id,id = None):
        self.id = id
        self.amount = amount
        self.payment_status = payment_status
        self.loan_id = loan_id