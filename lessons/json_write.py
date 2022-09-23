import json

with open("cars.json", 'a') as cars_file:
    cars = {"one": 1,
            "two": 2,
            "three": 3
            }
    json.dump(cars, cars_file)