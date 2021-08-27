
# Create-Library

Create your own library using pandas ,numpy and time module 
This python program helps you to search a book ,issue a book ,return a book  and also view a list of books.

> In this python program first we have to  import all require modules in our program
 
 ```sh
 import pandas as pd
import numpy as np
from collections import Counter
import time
```

Now we have to create a class for our program 
> Let's create a class of name Library
```sh
class Library
```
### Basically we have to create four method :-
- Issue book
- Return book
- Search book
- View list of book

The prototype of our program  will be like that we want to store all details in a dictionary (book_list) with key as reference id of book and value as a list of   details of book.([book_name,available or not ,Issue time,Return time,total book avaiable ,total book,penelity]).
### Reference id will help  us to perform all basic operations,
>Default constructor will create a dictiniory (book_list),read a csv file so that it can detect all the book's name and then sort then book name ,var d use counter module so that it can count the number of occurence of each book(remove duplicacy) and finally we will iterate over d variable and store all details in book_list.

```sh
self.book_list = {}
        print("welcome to our library")
        Bk = pd.read_csv("bohemian_literature.csv")
        Books = np.array(list(Bk.loc[Bk['title'].notnull(), "title"]))
        np.sort(Books)
        self.d = Counter(Books)
        for ref_id, book in enumerate(self.d.items()):
            # appending(i, j[0], j[1])
            book_name=book[0]
            count=book[1]
            l = [book_name, "AVAILABLE", [None] * count, [None] * count, count, count, 0]
            self.book_list[ref_id] = l
```

# Create method one by one:-
### Issue function:-
>- take reference id as input
>- search Reference id in book_list
>- if Reference id is present in book_list
>-- then we go inside 
>-- inside if condition we will check whether book is available or not
>-- if available then issue them and  store their issue time.
>- else print book is not present.



```bash
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

```
### Returned function :-
>- take reference id as input
>- if reference id  is present in book_list
>--    then check whether the book was already issued or not   
>- else print book is not found.
```     
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
```

### Search function:-
> it will search the book name in a book_list and return the data associated with that book
- it takes book name as an input
- if book name is present in book_list 
-- return the data related to that book.
- else print book not found
 ```sh
        print("*" * 140)
        print("Reference Id".ljust(20), "Book name".ljust(80), "status".ljust(20), "available copies".ljust(20), )
        print("*" * 140)

        for i, j in self.book_list.items():
            print(str(i).ljust(20), j[0][:60].ljust(80), j[1].ljust(20), j[-2])
            print("*" * 140)
        print()
 ```

 ### ViewList function:- 
 > it returns all the books present in book_list.
```sh
        book = input("enter book name")
        flag = True
        for i, j in self.book_list.items():
            if (book.title() or book) in j[0]:
                print("Referenence id is ", i, "Book name is --", j[0])
                flag = False
        if flag == True:
            print("No book found of this name")
```







        
        
