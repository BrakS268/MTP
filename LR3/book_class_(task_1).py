class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}"

    def to_dict(self):
        return {"title": self.title, "author": self.author}


if __name__ == "__main__":

    book1 = Book("Преступление и наказание", "Ф.М. Достоевский")
    book2 = Book("Мастер и Маргарита", "М.А. Булгаков")
    book3 = Book("Война и Мир", "Л.Н. Толстой")

    print("Список книг:")
    print(book1)
    print(book2)
    print(book3)

    print("\nКнига в формате словаря:")
    print(book1.to_dict())