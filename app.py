
def Add_a_Book():
    global Books
    while True:
        book=input("Enter a book that you want to add:").strip()
        if book=='':
            print("Book cannot empty")
        else:
           Books.append(book)
           print(f"added {book} to the library")
           break
   
def Borrow_a_Book():
    global Books
    while True:
       book=input("which book you want to borrow from libarary:")
       if book=='':
          print("Book cannot empty")
       else:
        
           if book in Books:
              Books.remove(book)
              print(f"{book} borrowed from libarary")
           else:
              print(f"{book} is not available in libarary")
              break
    
    
    
def Delete_a_Book():
    global Books
    while True:
       book=input("Enter the book that you want to delete:")
       if book=='':
           print("Book cannot be empty")
       else:
          Books.remove(book)
          print(f"{book} removed successfully from library")
          break
    

def Display_a_Book():
    global Books
    print("Books in the Library:")
    for book in Books:
        print("-",book)
    print("currently library is empty")
    
def submit_a_book():
    global Books
    while True:
       book = input("Enter the book that you want to submit to the library:")
       if book=='':
          print("book cannot be empty")
       else:
          Books.append(book)
          print(f"{book} was submitted successfully.")
          break
        
Books=[]
is_running=True

print("**********welcome to the Library Management system**************")
while is_running:
    print("############# ")
    print("1.Add a Book  ")
    print("2.Borrow a Book")
    print("3.Delete a Book")
    print("4.Display a Book")
    print("5.Submit a Book")
    print("6.Exit")

    choice=input("Enter a Choice (1-6):")
    
    if choice=='1':
        Add_a_Book()
        print("******************")
    elif choice=='2':
         Borrow_a_Book()
         print("******************")
    elif choice=='3':
        Delete_a_Book()
        print("******************")
    elif choice=='4':
        Display_a_Book()
        print("******************")
    elif choice=='5':
        submit_a_book()
        print("******************")
    elif choice=='6':
        is_running=False
    else:
        print("please enter correct choice")
print("Exiting program.Thank you for visiting my website")
        
        
        
        
        
        
