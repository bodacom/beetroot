# list_a = list(range(1,10+1))
# new_list = []
# print(type(new_list))
# for number in list_a:
#     squared_number = number**2
#     new_list.append(squared_number)
# print(list_a)
# print(new_list)

# a = ["d", "e", "f"]
# b = ["g", "i", "j"]
# new_list = []
# for i in a:
#     for j in b:
#         new_list.append(tuple([i, j]))
# print(new_list)

# 221018

brick = {"density": 1400, "thermal_conductivity":0.58, "cost":3830, "thickness":[250, 380, 520, 630]} 
aerated_concrete = {"density": 300, "thermal_conductivity":0.08, "cost":3300, "thickness":[200, 300, 375]}
hempcrete = {"density": 350, "thermal_conductivity":0.08, "cost":4500, "thickness":[200, 300, 400, 500]}
insulator_rockwool = {"density": 120, "thermal_conductivity":0.064, "cost":1668, "thickness":[50, 100, 120, 150, 200]}
insulator_EPS = {"density": 35, "thermal_conductivity":0.045, "cost":3800,"thickness":[50, 100, 120, 150, 200]}
a = [{'bearing_layer': 250, 'insulator_layer': 100},
 {'bearing_layer': 250, 'insulator_layer': 120},
 {'bearing_layer': 250, 'insulator_layer': 150},
 {'bearing_layer': 250, 'insulator_layer': 200}]
total_resistance = [{}]
for i in a:
    total_resistance.append(round(i['bearing_layer']*10**-3/brick["thermal_conductivity"] +
                            i['insulator_layer']*10**-3/insulator_rockwool["thermal_conductivity"], 2))

print(total_resistance)
