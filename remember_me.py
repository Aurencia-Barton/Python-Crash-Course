from pathlib import Path
import json

# def greet_user():
#     """Greet the user by name.""" 
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("\nWhat's is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"\nWe'll remember you when you come back, {username}!")

# greet_user()

# refactored code for remember_me.py
def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("\nWhat's is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name.""" 
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        # contents = json.dumps(username)
        # path.write_text(contents)
        print(f"\nWe'll remember you when you come back, {username}!")

greet_user()

