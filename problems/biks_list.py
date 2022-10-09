# list_a = list(range(1,10+1))
# new_list = []
# print(type(new_list))
# for number in list_a:
#     squared_number = number**2
#     new_list.append(squared_number)
# print(list_a)
# print(new_list)

a = ["d", "e", "f"]
b = ["g", "i", "j"]
new_list = []
for i in a:
    for j in b:
        new_list.append(tuple([i, j]))
print(new_list)
