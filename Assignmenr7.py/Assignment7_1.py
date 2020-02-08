

class BookStore:

    BookNo=0.0

    def __init__(self,val1,val2):
        BookStore.BookNo=BookStore.BookNo+1
        self.Name=val1
        self.Author=val2


    def Display(self):
        print("The Name is ",self.Name)
        print("The Author is ",self.Author)
        print("The Number of books are : ",self.BookNo)



BookName=input("Enter The Name Of the Book")
AuthorName=input("Enter The AuthorName")


obj1=BookStore(BookName,AuthorName)
obj1.Display()


obj2=BookStore(BookName,AuthorName)
obj2.Display()
