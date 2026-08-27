""""
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
  def __init__(self, breed, color):
    self.breed = breed
    self.color = color
    
  def bark(self):
    print(f"{self.name} says: BARK BARK BARK!!!")

class Cat(Animal):
  def __init__(self, breed, color):
    self.breed = breed
    self.color = color
    
  def meow(self):
    print(f"{self.name} says: Meow Meow")
    
    
resident_animals = [
  {}
]
    
while True: 
  print("\n--- Main Menu ---")
  print("1. Add a new animal")
  print("2. Display all animals")
  print("3. Adopt an animal")
  print("4. Exit")
    
  user_input = input("Select an option (1-4): ").strip()
  
  if user_input.isdigit() and 1 <= int(user_input) <= 4:
    user_choice = int(user_input)
    print(f"\nYou've Selected: {user_choice}\n")
    
  