class Book:
    def __init__(self,title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Name of {self.title} \n"
              f"Author of {self.author} \n"
              f"Year of create {self.year}")

info = Book("Nothing","By Daniyal","2024")
info.get_info()