class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price

    def display(self):
        print "\nTitle: %s\nAuthor: %s \nPrice: %d" % \
            (self.title, self.author, self.price)
