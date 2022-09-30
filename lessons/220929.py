class Phone:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

    def __call__(self, contact: str):
        print(f"Calling to {contact}")

my_phone = Phone("+38-098-048-64-05")
my_phone("+38-098-123-45-67")

cubic = lambda x: x**3
number = [1, 2, 3, 4, 5, 6, 7, 8]

mapped = list(map(cubic, number))

print(mapped)

str_numbers = list(map(str, number))

print(str_numbers)

aaa = list(map(print, number))

print(aaa)

total = [(1,2), (3,4), (5,6)]

list(map(lambda l: l[0] * l[1], total))