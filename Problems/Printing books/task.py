class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        # --------------
        # {title} by {author}. ${price}. [{book_id}]
        return f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'


# one_book = Book("LOS", "TITLE", 1000, 1)
# print(one_book)
