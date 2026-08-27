"""
ITS320 Week 65 - Critical Thinking Assignment
Animal Shelter Management system

This program manages a small animal shelter's animals. 
Users can add new animals, adopt an animal, 
or see all the animals that currently reside in the shelter.
"""
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def display_animal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")
    
    def has_birthday(self):
        self.age += 1
    
class Dog(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.color = color
      
    def bark(self):
        print(f"{self.name} says: BARK BARK BARK!!!")

class Cat(Animal):
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, species="Cat")
        self.breed = breed
        self.color = color
      
    def meow(self):
        print(f"{self.name} says: Meow Meow")
      
    
resident_animals = [
  {Cat("Noche", 12, "Bombay", "Black")},
  {Cat("Shadow", 12, "Bombay", "Black")},
  {Cat("Chibi", 2, "Mixed", "Black")},
  {Dog("Endo", 12, "Silkypoo Maltese", "Tan")},
  {Dog("Frankie", 3, "Doodle", "Tan")},
  {Dog("Oscar", 4, "Shepard Mix", "Black and Brown")}
]
    
while True: 
    print("\n--- Main Menu ---")
    print("1. Add a new animal")
    print("2. Display all animals")
    print("3. Adopt an animal")
    print("4. Exit")
      
    user_input = input("Select an option (1-4): ").strip()
    
    #validates user input is a digit and within acceptable range
    if user_input.isdigit() and 1 <= int(user_input) <= 4:
      choice = int(user_input)
      print(f"You've selected {choice}")
      print("-------------------------------")
      if choice == 4:
        break
      elif choice == 1:
        add_animal
      # elif choice == 2:
      #   view_animals()
      # elif choice == 3:
      #   adopt_animal()
    else:
      print("----------------------------")
      print("Please enter a numer 1 - 4: ")
      
    def add_animal():
        new_animal = {}
        animal_type = input("What type of animal is this?: ")
        if animal_type.lower() == "dog":
           add_dog()
        elif animal_type.lower() == "cat":
          add_cat()
        else: 
          print("We can only take in dogs or cats at this time.")
            
    def add_dog():
      new_dog = Dog()
      dog_name = input("What is the dog's name?: ")
      while dog_name == "":
        dog_name = input("Name cannot be empty. Please enter a name: ")
      new_dog.name = dog_name
      
      dog_age = input("How old is the dog?: ")
      while not dog_age.isdigit():
        dog_age = input("Please enter a numeric value for this dogs age: ")
      new_dog.age = int(dog_age) 
      
      dog_breed = input("What breed is the dog?: ")
      while dog_breed == "":
        dog_breed = input("Breed cannot be empty. Please enter a breed: ")
      new_dog.breed = dog_breed
      
    def add_cat():
      new_cat = Cat()
      cat_name = input("What is the cat's name?: ")
      while cat_name == "":
        cat_name = input("Name cannot be empty. Please enter a name: ")
      new_cat.name = cat_name
      
      cat_age = input("How old is the cat?: ")
      while not cat_age.isdigit():
        cat_age = input("Please enter a numeric value for this cats age: ")
      new_cat.age = int(cat_age) 
      
      cat_breed = input("What breed is the cat?: ")
      while cat_breed == "":
        cat_breed = input("Breed cannot be empty. Please enter a breed: ")
      new_cat.breed = cat_breed