# Task 2

# Extend Phonebook application

# Functionality of Phonebook application:

#     Add new entries 
#     Search by first name 
#     Search by last name 
#     Search by full name
#     Search by telephone number
#     Search by city or state
#     Delete a record for a given telephone number
#     Update a record for a given telephone number
#     An option to exit the program

 

# The first argument to the application should be the name of the phonebook. 
# Application should load JSON data, if it is present in the folder with application, 
# else raise an error. After the user exits, all data should be saved to loaded JSON.


import json


def initiate_phonebook():
    try:
        with open('phonebook.json', 'r+') as phonebook_file:
            try:
                phonebook = phonebook_file.read()
                phonebook = json.loads(phonebook)
            except json.JSONDecodeError:
                phonebook = {}
            return phonebook

    except FileNotFoundError:
        with open('phonebook.json', 'w') as phonebook_file:
            phonebook = {}
    return phonebook


def add_new_entry(phonebook: dict):
    
    phone_number = "+380" + correct_input(valid_phone_number, "Enter your phone number: +38-0", 
                 "Enter your phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")
    
    try:
        phonebook[phone_number]
        print('The entry already exists. Try to update or delete it.')
    except KeyError:
        
        first_name = correct_input(valid_first_or_last_name, "Enter your name: ", 
                                  "Name should be less than 50 characters and contains only letters").lower().title()
        
        last_name = correct_input(valid_first_or_last_name, "Enter your last name: ", 
                                  "Last name should be less than 50 characters and contains only letters").lower().title()
        
        full_name = first_name + " " + last_name
        
        state = correct_input(valid_city_or_state, "Enter your state: ").strip()
        city = correct_input(valid_city_or_state, "Enter your city: ").strip()
        
        phonebook[phone_number] = {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": full_name,
            "address": {
                "state": state,
                "city": city
            },
        }
        
        with open("phonebook.json", "w") as phonebook_file:
            json.dump(phonebook, phonebook_file, indent=4)


def search_by(phonebook: dict, key: str, searching_for: str):
    search_result = []
    
    if key == "phone_number":
        if phonebook.get(searching_for):
            search_result.append(searching_for)
        return search_result
    
    for phone_number in phonebook.keys():
        if key in ["state", "city"]:
            if phonebook[phone_number]["address"][key] == searching_for:
                search_result.append(phone_number)
                
        elif phonebook[phone_number][key] == searching_for:
            search_result.append(phone_number)
            
    return search_result

def delete_phone_number(phone_number: str, phonebook: dict):
    try:
        del phonebook[phone_number]
        print(f"Contact with phone number {phone_number} deleted.")
        with open("phonebook.json", "w") as phonebook_file:
            json.dump(phonebook, phonebook_file, indent=4)
    except KeyError:
        print("Phone number does not exist!")


def update_contact_info(phone_number: str, key: str, phonebook: str):
    try:
        phonebook[phone_number]
    except KeyError:
        print("Phone number is not exists!")
    
    if key == "phone_number":
        pass

    if key in ["state", "city"]:
        new_value = correct_input(valid_city_or_state, f"Enter your {key}: ").strip()
        phonebook[phone_number]["address"][key] = new_value

    if key in ["first_name", "last_name"]:
        new_value = correct_input(valid_first_or_last_name, f"Enter your {key.replace('_', ' ')}: ", 
                                "Name should be less than 50 characters and contains only letters").lower().title()
        phonebook[phone_number][key] = new_value
        
        contact = phonebook[phone_number]
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]

    if key == "full_name":
        new_first_name = correct_input(valid_first_or_last_name, f"Enter your first name: ", 
                                "Name should be less than 50 characters and contains only letters").lower().title()

        new_last_name = correct_input(valid_first_or_last_name, f"Enter your last name: ", 
                                "Name should be less than 50 characters and contains only letters").lower().title()
        
        contact = phonebook[phone_number]
        contact["first_name"] = new_first_name
        contact["last_name"] = new_last_name
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]
    
    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def valid_phone_number(phone_number: str):
  
    phone_number = phone_number.split('-') # ['96', '123', '40', '50']
    if len(phone_number) != 4:
        print("Not valid format!")
        return False
  
    format_of_elements = [2, 3, 2, 2]
    for index, digits in enumerate(phone_number):

        if not format_of_elements[index] == len(digits):
            print("Not valid format!")
            return False

        if not digits.isnumeric():
            print("Only digits can be in phone number!")
            return False
    
    return True

def valid_first_or_last_name(name: str):
    if len(name) > 50:
        return False
        print("Too many characters!")
    
    if not name.isalpha():
        print("Name must contains only alphabet letters!")
        return False
  
    return True

def valid_city_or_state(place_name: str):
    set_of_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "
    
    if "  " in place_name:
        print("Too many spaces!")
        return False
  
    if len(place_name) > 50:
        print("Too many characters!")
        return False
  
    if (place_name[0] == "-") or (place_name[-1] == "-"):
        print("- can not be in the first place")
        return False
      
    for letter in place_name:
        if letter not in set_of_characters:
            print("Should only contain alphabet or -")
            return False
  
    return True


def correct_input(valid_func, prompt: str, hint=False):
    valid = False
    
    if hint:
        print(hint)
    
    while not valid:
        value = input(prompt)
        valid = valid_func(value)
    
    return value


def perform(action):

    # Action == quit
    if action == 'q':
        return 0

    # Action == add entry
    elif action == 'a':
        add_new_entry(phonebook)

    # Action == search or search and show
    elif action == 's' or action == 'sh':
        search_criteria = {'p': 'phone_number',
                           'f': 'first_name',
                           'l': 'last_name',
                           'fn': 'full_name',
                           's': 'state',
                           'c': 'city'}
        key = input('''Search by:
        p - phone number
        f - first name
        l - last name
        fn - full name
        s - state
        c - city\n''')

        print(f'Search by {search_criteria[key]}.')
        value = input('Input value to search for: ')
        search_results = search_by(phonebook, search_criteria[key], value)
        
        if action == 'sh':
            for result in search_results:
                print(f'\nPhone:   {result}\n' + 
                        f'Name:    {phonebook[result]["full_name"]}\n' +
                        f'Address: {phonebook[result]["address"]["city"]}, {phonebook[result]["address"]["state"]}')
        else:
            print(f'Results were found: {len(search_results)}')
            for result in search_results:
                print(result)

    # Action == delete entry
    elif action == 'd':
        what_record = input('What entry do you want to delete?\nInput the phone number: ')
        delete_phone_number(what_record, phonebook)

    # Action == update
    elif action == 'u':
        what_contact = input('What contact do you want to update: ')
        key = input('What field do you want to update: ')
        update_contact_info(what_contact, key, phonebook)


def request_action():
    
    options = ['q', 'a', 's', 'sh', 'd', 'u']
    
    option = input('''
Choose and action:
    a - to add an entry
    s - to search by any of the fields
    sh - to search and show the entities 
    d - to delete an entry
    u - to update an entry
    q - to quit the phone book\n''')
    
    if option in options:
        return option
    else:
        print('\nAction does not exist.')
        return -1


# main program body

if __name__ == '__main__':

    phonebook = initiate_phonebook()

    while True:
        action = request_action()
        if action == -1:
            continue

        if perform(action) == 0:
            break
