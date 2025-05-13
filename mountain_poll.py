responses = {}

polling_active = True   #Set a flag which indicates that polling is active.

while polling_active:
    # Prompts for the person's name and their response. 
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #Store the response in the dictionary.
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False   #Set the flag to False to end the while loop.
        
    
    # Polling is complete. Show the results. 
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}!")
        
        
    
