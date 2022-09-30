import json


def open_phonebook():
    with open("phonebook.json", "r+") as phonebook_file:
        try:
            phonebook = phonebook_file.read()
            phonebook = json.loads(phonebook)
        except json.JSONDecodeError:
            phonebook = {}

    return phonebook

def valid_phone_number(phone_number: str):
    phone_number = phone_number.split('-')  # ['96', '123', '40', '50']
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

def add_new_entry(phonebook: dict):
    phone_number = "+380" + correct_input(valid_phone_number, "Enter your phone number: +380-",
                                      "Enter your phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")

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


def search_by(key: str, searching_for: str):
    search_result = []
    
    if key == "phone_number":
        if phonebook.get(searching_for):
            search_result.append(searching_for)
        return search_result
    
    for phone_number in phonebook.keys():
        if key in ["state", "city"]:
            if phonebook[phone_number]["address"][key] == searching_for:
                search_result.append(phone_number)
                
        if phonebook[phone_number][key] == searching_for:
            search_result.append(phone_number)
            
    return search_result

phonebook = open_phonebook()

# add_new_entry(phonebook)

search = search_by('first_name', 'Aron')

print(phonebook)
print(search)