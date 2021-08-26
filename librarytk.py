
import pandas as pd
import numpy as np
from collections import Counter
import time

class Library:
    book_list = {}
    # Bk = pd.read_csv("C:/Users/ACER/Downloads/jQuery/alexandra-bohemian-literature/alexandra-bohemian-literature/data/bohemian_literature.csv")
    Bk=pd.read_csv("library/bohemian_literature.csv")
    Books = np.array(list(Bk.loc[Bk['title'].notnull(), "title"]))
    np.sort(Books)
    d = Counter(Books)
    def __init__(self):
        print("welcome to our library")
        for ref_id, book in enumerate(self.d.items()):
            # appending(i, j[0], j[1])
            book_name=book[0]
            count=book[1]
            l = [book_name, "AVAILABLE", [None] * count, [None] * count, count, count, 0]
            self.book_list[ref_id] = l
    def issued(self):
        ref_id = int(input("Enter Reference Id"))
        if ref_id in self.book_list.keys():
            if self.book_list[ref_id][-2] == 0:
                print("Book Not Available")
            else:
                # print(self.book_list[])
                self.book_list[ref_id][2][self.book_list[ref_id][-3] - self.book_list[ref_id][-2]] = time.time()
                self.book_list[ref_id][-2] -= 1

                print("Book Issued")
                if self.book_list[ref_id][-2] == 0:
                    self.book_list[ref_id][1] = "NOT AVAILABLE"
        else:
            print("Reference id not found")

    def returned(self):
        ref_id = int(input("Enter Reference Id"))
        if ref_id in self.book_list.keys():
            if self.book_list[ref_id][-2] != self.book_list[ref_id][-3]:
                print("book returned")
                self.book_list[ref_id][1] == 'AVAILABLE'
                self.book_list[ref_id][-2] += 1

                a = self.book_list[ref_id][3][self.book_list[ref_id][-3] - self.book_list[ref_id][-2]] = time.time()
                print("total return time is", round(
                    self.book_list[ref_id][3][self.book_list[ref_id][-3] - self.book_list[ref_id][-2]] -self.book_list[ref_id][2][
                        self.book_list[ref_id][-3] - self.book_list[ref_id][-2]], 3), "sec")

            else:
                print("Books are already returned check your reference id!")
        else:
            print("book not found")

    def viewlist(self):
        print("*" * 140)
        print("Reference Id".ljust(20), "Book name".ljust(80), "status".ljust(20), "available copies".ljust(20), )
        print("*" * 140)

        for i, j in self.book_list.items():
            print(str(i).ljust(20), j[0][:60].ljust(80), j[1].ljust(20), j[-2])
            print("*" * 140)
        print()

    def search(self):
        book = input("enter book name")
        flag = True
        for i, j in self.book_list.items():
            if (book.title() or book) in j[0]:
                print("Referenence id is ", i, "Book name is --", j[0])
                flag = False
        if flag == True:
            print("No book found of this name")
library=Library()

while True:

    print("1)Isssue book")
    print("2)return book")
    print("3)search book")
    print("4) view list")
    print("5)exit")

    a=int(input("enter!!!!!"))
    if a==1:
        library.issued()
    elif a==2:
        library.returned()
    elif a==3:
        library.search()
    elif a==4:

        library.viewlist()
    else:
        print("Thankyou for Using Our Library")
        exit()
