import csv
import os

def add_book():
    title = title_validation()
    author = author_validation()
    pages = page_validation()
    print("{} by {} ({} 'Pages') added to Reading Tracker ".format(title, author, pages))
    books.append([title,author, pages,'c'])

def title_validation():
    title = input("Title: ")
    if title.isdigit() is True:
        print("Not a valid title input. Title can not be a number")
        print("Please try again!")
        return title_validation()
    elif len(title) == 0:
        print("Not a valid title input. Title can not be blanked")
        print("Please try again!")
        return title_validation()
    else:
        print(title.strip())
    return title.strip()

def author_validation():
    author = input("Author: ")
    if author.isdigit() is True:
        print("Not a valid author input. Author can not be a number")
        print("Please try again!")
        return author_validation()
    elif len(author) == 0:
        print("Not a valid title input. Author can not be blanked")
        print("Please try again!")
        return author_validation()
    else:
        print(author.strip())
    return author.strip()

def page_validation():
    pages = input("Pages:")
    if pages.isdigit() is False:
        print("Invalid input; enter a valid number")
        return page_validation()
    elif int(pages) <= 0:
        print("Number must be > 0")
        return page_validation()
    return int(pages)

def num_validation():
    num = input("Enter the number of a book to mark as completed ")
    if num.isdigit() is False:
        print("Invalid input; enter a valid number")
        return num_validation()
    elif int(num) <= 0:
        print("Number must be > 0")
        return num_validation()
    elif int(num)>len(books):
        print("Invalid Book Number")
        return num_validation()
    return int(num)

def counter():
    c=0
    p=0
    b=0
    for book in books:
        c=c+1
        if book[3]=="r":
            print("*{:<2}. {:<40} by {:<20} {:<5} Pages".format(c,book[0],book[1],book[2]))
            b=b+1
            p=p+int(book[2])
        else:
            print(" {:<2}. {:<40} by {:<20} {:<5} Pages".format(c,book[0],book[1],book[2]))
    if b==0:
        print("No required books")
        main()
    else:
        print("You need to read {} pages in {} books".format(p,b))

def mark_book():
    counter()
    num = num_validation()
    if books[num-1][3]=="c":
        print("That book is already completed")
    else:
        books[num-1][3]="c"
        print("{} by {} completed!".format(books[num-1][0],books[num-1][1]))

def save_books():
    file = open('books.csv', 'w', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(books)

def list_books():
    c=0
    for book in books:
        c=c+1
        if book[3]=="r":
            print("*{:<2}. {:<40} by {:<20} {:<5}Pages".format(c,book[0],book[1],book[2]))
        else:
            print(" {:<2}. {:<40} by {:<20} {:<5}Pages".format(c,book[0],book[1],book[2]))

def main():
    while True:
        print("Menu:")
        print("L - List all books")
        print("A - Add new book")
        print("M - Mark a book as completed")
        print("Q - Quit")
        choice = input(">>> ").upper()
        if choice == "L":
            list_books()
        elif choice == "A":
            add_book()
        elif choice == "M":
            mark_book()
        elif choice == "Q":
            save_books()
            print("{} books saved to books.csv".format(len(books)))
            print("So many books, so little time. Frank Zappa")
            break
        else:
            print("Invalid menu choice")
            
print("Reading Tracker 1.0 - by Lindsay Ward")
with open('books.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    books = list(reader)
    print(len(books),"books loaded")
main()

