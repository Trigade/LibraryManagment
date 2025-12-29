class Members:
    def __init__(self,first_name,last_name,email,phone,join_date = None,membership_status = None,id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone 
        self.join_date = join_date
        self.membership_status = membership_status

