pets = ['dog', 'cat', 'fish', 'lizard', 'hamster'] #list of pets
print(pets) #print the list of pets

while pets:  #while loop that removes every instance of 'cat' from the list
    pets.remove('cat') #removes the first occurrence of 'cat' from the list and every other instance of 'cat' until the list is empty
    
    print(pets) #prints the new list of pets which no longer contains 'cat'
