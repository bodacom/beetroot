import task2

phonebook = task2.initiate_phonebook()

print(task2.search_by(phonebook, 'last_name', 'Pishchaniuk'))

# print(phonebook)
# print(type(phonebook))

# for key, value in phonebook.items():
#     print(key, value)

# import json

# # Data to be written
# dictionary = {"id": "04", "name": "sunil", "department": "HR"}

# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
# print(json_object)

