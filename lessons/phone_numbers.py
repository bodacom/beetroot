import json


def open_phonebook():
    with open("phonebook.json", "r+") as phonebook_file:
        try:
            phonebook = phonebook_file.read()
            phonebook = json.loads(phonebook)
        except json.JSONDecodeError:
            phonebook = {}
    
    return phonebook


# Перевірки у функції (опціонально)
# delete_contact(phone_number)
# update_contact(phone_number)

# Перевірки для add_new_entry(): перевірка на кількість символів в ПІ та адресі, номер телефону
# щоб не було пустих символів. Перевірка унікальності запису (контакта)

# def find_by_first_name(first_name)
# return:
"""
Контакти що знайдені по first_name: value

1. First name: ---
   Last name: ---
   
2. 

3.
"""
# while True:<--- це програма (додаток) в якому буде меню. Вийти з додатку це має бути опція меню 


def add_new_entry():
    phonebook = open_phonebook()
    
#     phone_number = input("Enter your phone number: ")
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     full_name = first_name + " " + last_name
#     state = input("Enter your state: ")
#     city = input("Enter your city: ")
    phone_number = "+3809634240"
    first_name = "Andrii"
    last_name = "Kondratyuk"
    full_name = first_name + " " + last_name
    state = "Kyiv oblast"
    city = "Kyiv"
    
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