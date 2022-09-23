import json

with open("cars.json", 'r') as cars_file:
    cars = cars_file.readlines()
    print(cars)
    for car in cars:
        car_j = json.loads(car.rstrip())
        print(car_j)
        print(type(car_j))
        print(id(car_j))