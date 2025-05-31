prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)" # This line prompts the user to enter a city name or 'quit' to end the program.

while True: # This loop continues forever until the user enters 'quit'.
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!") # This line prints a message that includes the city name.
