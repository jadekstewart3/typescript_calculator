"""
ITS320 Week 6 - Critical Thinking Assignment
Animal Shelter Management System

This program manages a small animal shelter's animals. Users can add new
animals, adopt an animal, or view all animals that currently reside in the
shelter.
"""
#import abstract base class
from abc import ABC, abstractmethod


class Animal(ABC):
#Abstract base class for every animal housed in the shelter.

 #Initialize the attributes shared by every animal."
    def __init__(self, name, age, species):
        self.__species = species
        self.name = name  # assigned through the validating setter below
        self.age = age    # assigned through the validating setter below

    @property
    def name(self):
        return self.__name

  #validate name value prior to storing it
    @name.setter
    def name(self, value):
        if not str(value).strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

  #validates age prior to storing it
    @age.setter
    def age(self, value):
        if int(value) < 0:
            raise ValueError("Age cannot be negative")
        self.__age = int(value)

    def has_birthday(self):
        self.age = self.age + 1

    def display_animal_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")

    @abstractmethod
    def speak(self):
        ...


#A dog available for adoption from the shelter.
class Dog(Animal):

    #Initialize a dog, fixing its species as 'Dog'.
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, species="Dog")
        self.__breed = breed
        self.__color = color

    #return the dogs breed
    @property
    def breed(self):
        return self.__breed

   #return the dogs color
    @property
    def color(self):
        return self.__color
    
    #return the dog sound
    def speak(self):
        return f"{self.name} says: BARK BARK BARK!!!"

    #display dog info
    def display_animal_info(self):
        super().display_animal_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")


  #A cat available for adoption from the shelter.
class Cat(Animal):
   #Initialize a cat, fixing its species as 'Cat'.
    def __init__(self, name, age, breed, color):
        super().__init__(name, age, species="Cat")
        self.__breed = breed
        self.__color = color

    #Return the cat's breed.
    @property
    def breed(self):
        return self.__breed

    #Return the cat's color.
    @property
    def color(self):
        return self.__color

    #Return the sound a cat makes.
    def speak(self):
        return f"{self.name} says: Meow Meow"

    #Print the cat's shared attributes plus its breed and color.
    def display_animal_info(self):
        super().display_animal_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")


# The shelter's collection of current residents.
resident_animals = [
    Cat("Noche", 12, "Bombay", "Black"),
    Cat("Shadow", 12, "Bombay", "Black"),
    Cat("Chibi", 2, "Mixed", "Black"),
    Dog("Endo", 12, "Silkypoo Maltese", "Tan"),
    Dog("Frankie", 3, "Doodle", "Tan"),
    Dog("Oscar", 4, "Shepard Mix", "Black and Brown"),
]


#Prompt until the user types a non-empty value, then return it.
def prompt_non_empty(prompt, error_message):
    value = input(prompt).strip()
    while value == "":
        value = input(error_message).strip()
    return value


#Prompt until the user types a non-negative whole number, then return it.
def prompt_positive_int(prompt, error_message):
    value = input(prompt).strip()
    while not value.isdigit():
        value = input(error_message).strip()
    return int(value)


#Ask what kind of animal is arriving and add a new dog or cat.
def add_animal():
    animal_type = input("What type of animal is this?: ").strip().lower()
    if animal_type in ("dog", "cat"):
        add_dog_or_cat(animal_type)
    else:
        print("We can only take in dogs or cats at this time.")


#Collect the details for a dog or cat and store it in the shelter.
def add_dog_or_cat(animal_type):
    name = prompt_non_empty(
        f"What is the {animal_type}'s name?: ",
        "Name cannot be empty. Please enter a name: ",
    )
    age = prompt_positive_int(
        f"How old is the {animal_type}?: ",
        f"Please enter a numeric value for this {animal_type}'s age: ",
    )
    breed = prompt_non_empty(
        f"What breed is the {animal_type}?: ",
        "Breed cannot be empty. Please enter a breed: ",
    )
    color = prompt_non_empty(
        f"What color is the {animal_type}?: ",
        "Color cannot be empty. Please enter a color: ",
    )
    animal_class = Dog if animal_type == "dog" else Cat
    resident_animals.append(animal_class(name, age, breed, color))
    print(f"{name} has been added to the shelter!")


#Print every animal that currently resides in the shelter.
def view_animals():
    if not resident_animals:
        print("There are currently no animals in the shelter!")
        return
    for animal in resident_animals:
        print(f"{animal.species}:")
        animal.display_animal_info()
        print("-------------------------------")


#Return the resident animal whose name matches, or None if there is none.
def find_animal(user_input):
    for animal in resident_animals:
        if animal.name.lower() == user_input.lower():
            return animal
    return None


#Adopt an animal out by name and remove it from the shelter.
def adopt_animal():
    user_input = input(
        "Please enter the name of the animal you would like to adopt: "
    ).strip()

    animal = find_animal(user_input)
    if animal is None:
        print("I'm sorry we don't have that animal as a resident.")
    else:
        resident_animals.remove(animal)
        print(f"Yay {animal.name} has found their forever home!!")
        print(animal.speak())


#Run the shelter menu until the user chooses to exit.
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new animal")
        print("2. Display all animals")
        print("3. Adopt an animal")
        print("4. Exit")

        user_input = input("Select an option (1-4): ").strip()

        # validates user input is a digit and within the acceptable range
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            choice = int(user_input)
            print(f"You've selected {choice}")
            print("-------------------------------")
            if choice == 4:
                break
            elif choice == 1:
                add_animal()
            elif choice == 2:
                view_animals()
            elif choice == 3:
                adopt_animal()
        else:
            print("----------------------------")
            print("Please enter a number 1 - 4: ")


main_menu()
