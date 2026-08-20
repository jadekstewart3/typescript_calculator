""""
ITS320 Week 5 - Critical Thinking Assignment
Library Management System

This program manages a small library's book inventory. Users can add new
books, borrow books, return books, and view the current inventory through
a simple text menu.
"""
#intialize list containing books in inventory
book_inventory =[
  {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies_available": 3},
  {"title": "Dune", "author": "Frank Herbert", "copies_available": 2},
  {"title": "1984", "author": "George Orwell", "copies_available": 0},
  {"title": "Oryx and Crake", "author": "Margaret Atwood", "copies_available": 6}
  ]

#displays main menu and accepts valid user input
def main_menu():
  while True:
    print("----- Maintain inventory ----")
    print("1. Add a book to inventory")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. View inventory")
    print("5. Exit")
    
    user_input = input("Select option 1-5: ").strip()
    
    #validates user input is a digit and within acceptable range
    if user_input.isdigit() and 1 <= int(user_input) <= 5:
      choice = int(user_input)
      print(f"You've selected {choice}")
      print("-------------------------------")
      if choice == 5:
        break
      elif choice == 1:
        add_new_book()
      elif choice == 2:
        borrow_book()
      elif choice == 3:
        return_book()
      elif choice == 4:
        view_inventory()
    else:
      print("----------------------------")
      print("Please enter a numer 1 - 5: ")
  
#adds a new book to inventory  
def add_new_book():
  new_book = {}

  # Loop until we get a non-empty title
  book_title = input("Please enter the title of your book: ").strip()
  while book_title == "":
    book_title = input("Title cannot be empty. Please enter the title of your book: ").strip()
  new_book["title"] = book_title

  # Loop until we get a non-empty author
  book_author = input("Please enter the author's name: ").strip()
  while book_author == "":
    book_author = input("Author cannot be empty. Please enter the author's name: ").strip()
  new_book["author"] = book_author

  # Loop until we get a valid positive number of copies
  num_copies = input("Please enter the number of copies available: ").strip()
  while not (num_copies.isdigit() and int(num_copies) > 0):
    num_copies = input("Please enter a whole number greater than 0: ").strip()
  new_book["copies_available"] = int(num_copies)

  book_inventory.append(new_book)
  print(f"\nYay! You added '{book_title}' to inventory!\n")
  
#allows user to view all books currently in inventory
def view_inventory():
  if not book_inventory:
      print("Inventory is empty!")
  for book in book_inventory:
      print(f"Title: {book["title"]}")
      print(f"Author: {book["author"]}")
      print(f"Copies Available: {book["copies_available"]}")
      print("-------------------------------")

#returns matching book dictionary, None if not found
def find_book(title):
  for book in book_inventory:
    if book["title"].lower() == title.lower():
      return book
  return None

#reduces copies_available if book is in inventory
#if book is not in inventory, displays message to user
def borrow_book():
  user_input = input("Please enter the title of the book you would like to borow: ").strip()
  
  book = find_book(user_input)
  if book is None:
    print("Sorry, that book is not in inventory.")
    return

  if book["copies_available"] > 0:
    book["copies_available"] -= 1
    print("Hooray! Happy Reading!")
  else: 
    print("Sorry there are no copies available to borrow")
      
# adds to copies_available if book is already in inventory
def return_book():
  user_input = input("What is the title of the book you are returning?: ").strip()

  book = find_book(user_input)
  if book is not None:
    book["copies_available"] += 1
    print("Thank you for returning your book!")
  else:
    print("Sorry, that book is not in inventory. Perhaps it belongs to a different library?")
  
main_menu()