class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def summary (self):
        return f"Bokens titeln är {self.title} och skrevs av {self.author}. "
    