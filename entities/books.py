class Books:
    def __init__(self,title,isbn,publish_year,stock_quantity,publisher_id,category_id,author_id,id = None):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.publish_year = publish_year
        self.stock_quantity = stock_quantity
        self.publisher_id = publisher_id
        self.category_id = category_id
        self.author_id = author_id