# Start with users that need to verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'bob', 'charlie']
confirmed_users = []


# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop() #removes the last user from the unconfirmed_users list and assigns it to current_user.
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) #adds the current_user to the confirmed_users list.
    
    # Display all confirmed users.
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
    
    
    