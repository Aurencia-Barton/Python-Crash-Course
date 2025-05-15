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