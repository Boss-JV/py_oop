class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")
        
b1 = Book("RC design", "Mongkol", 450)
b2 = Book("Mechanics of material", "Ferdinand P.Beer", 975)

b1.summary()
b2.summary()