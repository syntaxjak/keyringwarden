import keyring
import random
import json


# List of preprogrammed responses
responses = [
    "Welcome, sire, your keyrings:",
    "Yes sire, your keys are here",
    "Hail my sire, I have your keys as you requested",
    "Salutations, sire, I was not sleeping, here is your keyring"
]

# Randomly select a response
response = random.choice(responses)

def save_key(service, name):
    keys_file = 'keys.json'
    
    # Try to load existing keys
    try:
        with open(keys_file, 'r') as file:
            keys = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        keys = []
    
    # Add the new key info
    keys.append({'service': service, 'name': name})
    
    # Write the updated keys list to the file
    with open(keys_file, 'w') as file:
        json.dump(keys, file)

def add_key():
    service = input("Enter service: ")
    name = input("Enter name: ")
    key = input("Enter key: ")
    keyring.set_password(service, name, key)
    save_key(service, name)
    print("Your key has been saved!")

def remove_key():
    service = input("Enter service: ")
    name = input("Enter name: ")
    try:
        keyring.delete_password(service, name)
        print("Your key has been removed!")
    except keyring.errors.PasswordDeleteError:
        print("The specified key was not found!")

def list_keys():
    keys_file = 'keys.json'
    
    # Try to load and display keys
    try:
        with open(keys_file, 'r') as file:
            keys = json.load(file)
            for key_info in keys:
                service = key_info['service']
                name = key_info['name']
                
                # Retrieve and display the key for each stored service-name pair
                key = keyring.get_password(service, name)
                print(f"\t{service}/{name}: {key if key else 'Key not found'}")
                
    except (FileNotFoundError, json.JSONDecodeError):
        print("No keys found.")
        
while True:
    print(f'\nThe Keyring Warden greets you: "{response}"')
    print("1. Add a new key")
    print("2. Remove an existing key")
    print("3. List keys")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_key()
    elif choice == "2":
        remove_key()
    elif choice == "3":
        list_keys()
    elif choice == "4":
        print("Leaving The Keyring Warden.")
        break
    else:
        print("Invalid choice.")