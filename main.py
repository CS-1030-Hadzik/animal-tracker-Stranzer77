from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    bird = Animal("Big Bird", "Ostrich") 
    # TODO: Print the Animal instance
    print(bird)
    # TODO: Call the method to make a generic animal sound
    bird.speak()

    # TODO: Create an instance of the Dog class
    fido = Dog("Fido", "Canine", "Hound")
    # TODO: Print the Dog instance
    print(fido)
    # TODO: Call the method to make the dog-specific sound
    fido.speak()

    # TODO print out all the animals
    animals = Animal.get_all_animals()
    for animal in animals:
        print(animal)
