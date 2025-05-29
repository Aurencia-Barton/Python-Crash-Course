class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age): # this method is called when an instance of the class is created.
        """Initialize name and age attributes."""
        self.name = name  # This line initializes the name attribute of the Dog class.
        self.age = age # This line initializes the age attribute of the Dog class.

    def sit(self): # This method simulates the dog sitting.
        """Simulates a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self): # This method simulates the dog rolling over.
        """Simulates rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy',3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


# my_dog.roll_over()


