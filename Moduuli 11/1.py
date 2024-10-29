class Publication:
    def __init__(self, name):
        self.name = name
class Book(Publication):
    def __init__(self, author, page_count, name):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def info(self):
        print(f"publisher: {self.name}, Author: {self.author}, Pages: {self.page_count}")

class Magazine(Publication):
    def __init__(self, editor, name):
        super().__init__(name)
        self.editor = editor
    def info(self):
        print(f"publisher: {self.name}, Editor: {self.editor}")
book1 = Book("Vincent van Gogh", 100, "Marvel")
magazine1 = Magazine("Edgar Allan Poe", "The sun")
book1.info()
magazine1.info()