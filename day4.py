# CLI application that keeps a record of animals I own
# Animal types: Animal, Cat, Dog
#           - Attributes: Name, Age
# Want to store our animal information to a file
# Upon restarting application, want to load animal data from file

# Importing animal module
import animal
import re
from pymongo import MongoClient
import logging

logging.basicConfig(filename='animal.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p::')
'''
DEBUG    - Detailed info, typically of interest only when diagnosing problems
INFO     - Confirmation that things are working as usual
WARNING  - An indication that something unexpected happened, or some problem may occur in the near future
ERROR    - Due to a serious problem, the application has not been able to perform some function
CRITICAL - A serious error indicating the program may be unable to continue
'''


# Used to create animal object from user-inputted values
def add_animal() -> animal.Animal:
    logging.debug("Entering add_animal")
    # Input verification
    while True:
        try:
            print("Hello! Please select type of animal to input:")
            print("\t a) Generic animal")
            print("\t c) Cat")
            print("\t d) Dog")
            typeAnimal = input(">>>")

            
            if not typeAnimal == 'c' and not typeAnimal == 'd' and not typeAnimal == 'a':
                raise ValueError('Invalid input for animal type')
            else:
                break
        except ValueError:
            print("Oh no! Please enter a valid type for animal! ('a', 'c', 'd')")
            pass

    while True:
        try:
            print("\n\nEnter animal name:")
            name = input(">>>")
            if not re.search(r"[,\.\\\*\-]", name) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in your name for your animal!")
            logging.info("ValueError caught: User entered special char in name")


    while True:
        try:
            print("\n\nEnter animal age:")
            age = int(input(">>>"))
            break
        except ValueError:
            print("Oh no! You must enter a number for the age! Try again!")

    if typeAnimal == 'a':
        newAnimal = animal.Animal(name, age)
    elif typeAnimal == 'c':
        newAnimal = animal.Cat(name, age)
    else:
        newAnimal = animal.Dog(name, age)
    
    return newAnimal


# Save animal list to saved_animals.txt
def save_animals(lst_Animals):
    logging.debug("Entering save_animals")
    f = open('saved_animals.txt', 'w')

    for animal in lst_Animals:
        f.write(animal.name + ',' + str(animal.age) + ',' +  animal.animal_type + "\n")

    f.close()

# Load animals from saved_animals.txt
def load_animals():
    logging.debug("Entering load_animals")
    f = open('saved_animals.txt', 'r')
    lst_animals = []
    for line in f:
        if line == '':
            break

        animal_data = line.split(',')
        if animal_data[2].strip() == 'Generic':
            newAnimal = animal.Animal(animal_data[0], animal_data[1])
        elif animal_data[2].strip() == 'Cat':
            newAnimal = animal.Cat(animal_data[0], animal_data[1])
        else:
            newAnimal = animal.Dog(animal_data[0], animal_data[1])
        
        lst_animals.append(newAnimal)
    f.close()
    return lst_animals

# Function to save an animal to collection in MongoDB
def save_to_db(anim, animaldb):
    logging.debug("Entering save_to_db")
    dict_Animal = {
        "name" : anim.name,
        "age" : anim.age,
        "type" : anim.type
    }

    animaldb.animals.insert_one(dict_Animal)
    logging.info("Successfully added an object to database")

#Main function
def main():
    check_conn = True
    try:
        client = MongoClient("127.0.0.1", 27017)

        animaldb = client.animal
    except BaseException:
        print("Sorry, could not connect!")
        check_conn = False

    print("Welcome to the Animal Journal")

    lst_Animals = load_animals()
    while True:
        try:
            print("Please select an option:")
            print("\ta) Add new Animal")
            print("\ts) Save all animals to MongoDB (only run once!)")
            print("\tq) Quit")

            option = input(">>>")

            logging.debug("User inputted %s", option)

            if option == 'q':
                break

            elif option == 's' and check_conn:
                try:
                    for anim in lst_Animals:
                        save_to_db(anim, animaldb)
                except BaseException:
                    print("Sorry, could not make a good connection to db!")

            elif option == 's' and not check_conn:
                print("Sorry! Connection to db not established")

            elif option == 'a':
                lst_Animals.append(add_animal())

            else:
                raise ValueError('Invalid menu option')

        except ValueError as ve:
            print(ve)
            print("Invalid option! Please try again!")
    
    for animal in lst_Animals:
        print(animal, type(animal))
    
    save_animals(lst_Animals)


if __name__ == '__main__':
    main()





