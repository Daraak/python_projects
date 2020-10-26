import os


class Library:

    def __init__(self, library_name, *books):
        self.name = library_name
        self.books = books
        self.adding = ""
        self.books_avail = ""
        self.libra = {'Library Name': str(self.name), "Books": self.books}
        with open('library.txt', 'a+') as generate_lib:
            for i in generate_lib:
                if self.books == i:
                    self.books_avail = 'Available'
                    quit()
            if self.books_avail != 'Available' and self.name is not None and self.books is not None:
                generate_lib.write("{0}\n".format(str(self.libra)))
        self.lent = dict()
        self.found = None

    @staticmethod
    def display_books():
        with open('library.txt', 'r') as display:
            displaying = display.read()
            print(displaying)

    def lend_books(self):
        with open('library.txt', 'r') as reading:
            print(reading.read())
        lender_book = input('Which book you wanna lend; Chose the name accordingly (only one):- ')
        lender_name = input('Tell me your name:- ')
        if lender_book is not None and lender_name is not None:
            self.lent[lender_name.upper()] = lender_book.upper()
            with open('lenders.txt', 'r+') as search_file:
                for i in search_file:
                    if lender_book.upper() in i:
                        print('Sorry the book is not available; Lent by someone!')
                        self.found = "Found"
                if self.found != "Found":
                    with open("lenders.txt", 'a') as appending:
                        appending.write(f"{str(self.lent)} \n")

    @staticmethod
    def add_books():
        adding = input('Which book you want to add:- ')
        if adding is not None:
            with open('library.txt', 'a') as appending:
                appending.write(f"New book added: {adding.capitalize()}" + '\n')
            print('Thanks a lot for providing a book to out library!')

    def return_books(self):
        returner = input('Tell me your name:- ')
        returning = input('Which book you are here to return:- ')
        with open('lenders.txt', 'r') as reading:
            with open('temp.txt', 'w') as writing:
                for line in reading.readlines():
                    if returner.upper() in line and returning.upper() in line:
                        self.found = "found"
                    elif returner.upper() not in line and returning.upper() not in line:
                            writing.write(line)
                if self.found != 'found':
                    print("No entry matches with the provided name and book;")
        with open('lenders.txt', 'w') as writing:
            with open('temp.txt', 'r') as reading:
                for line in reading.readlines():
                    writing.write(line)
                print('Thank you for returning the book;')
        os.remove('temp.txt')

    def on_start(self) -> object:
        print('\n 1.Display Books', '\n 2.Lend Book', '\n 3.Add Book', '\n 4.Return Book')
        a = input('\n Chose the number of the given options accordingly:- ')
        if a == str(1):
            return self.display_books()
        elif a == str(2):
            return self.lend_books()
        elif a == str(3):
            return self.add_books()
        elif a == str(4):
            return self.return_books()
        else:
            print('Wrong Input! Try Again;')


x = 'y'
while x == "y":
    ask = input('Are you creating a new library [y | n]:- ')
    if ask == 'y':
        making_lib = input("Enter your library name:- ")
        making_lib1 = input("Enter the books you wanna add in your library \n E.x. [a, b, c]:- ")
        lib = Library(making_lib, making_lib1)
        lib.on_start()
    elif ask == 'n':
        lib = Library(None, None)
        x = 'n'
        n = 'y'
        while n == 'y':
            b = input('\nDo you want to continue to the options; \n[Continue = y | Exit = n]:- ')
            if b == 'y':
                lib.on_start()
            elif b == 'n':
                n = 'n'
                print('See yah! Will meet soon;')
            else:
                print('Wrong input! Try again;')
    else:
        print('Wrong input! Try Again;')