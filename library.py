books=[]
book=input("enter the name of book you own : ")
books.append(book)
book=input("enter the name of anather book you own(or press'enter' to skip)")
if book:
    books.append(book)
print (f"your library : {books} ")
Wish_book=[]
wish_books=input("enter the name of a book you wish to have it in the future : ")  
Wish_book.append(wish_books)   
wish_book=input ("enter the name of another book you wish to have (or press 'enter' to skip : ) ") 
if wish_book:  
    Wish_book.append(wish_book)  
print (f"your wishlist : {Wish_book}")
book_have=input ("enter the name of book from your wishlist that you've a required or press 'enter' to skip : ")
if book_have in Wish_book:
    Wish_book.remove(book_have)
    books.append(book_have)
print ("\nupdate library",books)    
print ("\nupdate wishlist",Wish_book)
donat_book=input("enter the name of book from your libraryyou wish to donat it or (press 'enter ' to skip : ")
if donat_book in books:
    books.remove(donat_book)
print ("final library is : ",books)
