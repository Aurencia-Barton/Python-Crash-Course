prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit': # This loop continues until the user enters 'quit'.
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True
while active: # As long as the active variable remains True, the loop continues running.
    message = input(prompt)
    
    if message == 'quit': # If the user enters 'quit', the loop ends.
        active = False
    else:
        print(message)