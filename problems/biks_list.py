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

# brick = {"density": 1400, "thermal_conductivity":0.58, "cost":3830, "thickness":[250, 380, 520, 630]} 
# aerated_concrete = {"density": 300, "thermal_conductivity":0.08, "cost":3300, "thickness":[200, 300, 375]}
# hempcrete = {"density": 350, "thermal_conductivity":0.08, "cost":4500, "thickness":[200, 300, 400, 500]}
# insulator_rockwool = {"density": 120, "thermal_conductivity":0.064, "cost":1668, "thickness":[50, 100, 120, 150, 200]}
# insulator_EPS = {"density": 35, "thermal_conductivity":0.045, "cost":3800,"thickness":[50, 100, 120, 150, 200]}
# a = [{'bearing_layer': 250, 'insulator_layer': 100},
#  {'bearing_layer': 250, 'insulator_layer': 120},
#  {'bearing_layer': 250, 'insulator_layer': 150},
#  {'bearing_layer': 250, 'insulator_layer': 200}]
# total_resistance = [{}]
# for i in a:
#     total_resistance.append(round(i['bearing_layer']*10**-3/brick["thermal_conductivity"] +
#                             i['insulator_layer']*10**-3/insulator_rockwool["thermal_conductivity"], 2))

# print(total_resistance)

# brick = {"density": 1400, "thermal_conductivity":0.58, "cost":3830, "thickness":[250, 380, 520, 630]} 
# insulator_rockwool = {"density": 120, "thermal_conductivity":0.064, "cost":1668, "thickness":[50, 100, 120, 150, 200]}
# new_set = [{"brick_thickness":thickness,"insulator_rockwool_thickness":insulator} for thickness in brick["thickness"] for insulator in insulator_rockwool["thickness"]]

# for index, element in enumerate(new_set):
#     r_value = round(element["brick_thickness"]*10**-3/brick["thermal_conductivity"] + element["insulator_rockwool_thickness"]*10**-3/insulator_rockwool["thermal_conductivity"], 2)
#     new_set[index]['R-value'] = r_value

# print('[', new_set[0], sep='')
# for element in new_set[1:-1]:
#     print(' ', element, sep='')
# print(' ', new_set[-1], ']', sep='')

# min_R_value = min(dict_el["R-value"] for dict_el in new_set)
# print(min_R_value)

# На виході хочу отримати щось типу списку з словників:
# [{'brick_thickness': 250, 'insulator_rockwool_thickness': 50, 'R-value':1.99},
#  {'brick_thickness': 250, 'insulator_rockwool_thickness': 100, R-value':2.31},
#  {'brick_thickness': 250, 'insulator_rockwool_thickness': 120, R-value':2.77},
#  {'brick_thickness': 250, 'insulator_rockwool_thickness': 150, R-value':3.56},
# ...]

# general_meet = [{'hempcrete_thickness': 500,
#                  'insulator_EPS_thickness': 120,
#                  'R-value': 8.92,
#                  'mass': 179.2,
#                  'cost': 2706.0},
#                  {'hempcrete_thickness': 500,
#                  'insulator_EPS_thickness': 150,
#                  'R-value': 9.58,
#                  'mass': 180.25,
#                  'cost': 2820.0},
#                  {'hempcrete_thickness': 500,
#                  'insulator_EPS_thickness': 200,
#                  'R-value': 10.69,
#                  'mass': 182.0,
#                  'cost': 3010.0}]

# min_R_value = min(dict_el["R-value"] for dict_el in general_meet)
# print(min_R_value)


# Initial data
brick_thickness = [250, 380, 520, 630]
aerated_concrete_thickness = [200, 300, 375]
hempcrete_thickness = [200, 300, 400, 500]
insulator_thickness = [50, 100, 120, 150, 200]
# Physical-mechanical and economical values: density kg/m3; thermal_conductivity coefficient W/m*K; cost UAH/m3, thickness in mm
brick = {"density": 1400, "thermal_conductivity": 0.58, "cost": 3830, "thickness": [250, 380, 520, 630]}
aerated_concrete = {"density": 300, "thermal_conductivity": 0.08, "cost": 3300, "thickness": [200, 300, 375]}
hempcrete = {"density": 350, "thermal_conductivity": 0.08, "cost": 4500, "thickness": [200, 300, 400, 500]}
insulator_rockwool = {"density": 120, "thermal_conductivity": 0.064, "cost": 1668,
                      "thickness": [50, 100, 120, 150, 200]}
insulator_EPS = {"density": 35, "thermal_conductivity": 0.045, "cost": 3800, "thickness": [50, 100, 120, 150, 200]}

# Combination of layers with insulators:
brick_rockwool = [{"brick_thickness": brick, "insulator_rockwool_thickness": insulator} for brick in brick["thickness"]
                  for insulator in insulator_rockwool["thickness"]]
brick_EPS = [{"brick_thickness": brick, "insulator_EPS_thickness": insulator} for brick in brick["thickness"] for
             insulator in insulator_EPS["thickness"]]

aerated_concrete_rockwool = [{"aerated_concrete_thickness": brick, "insulator_rockwool_thickness": insulator} for brick
                             in aerated_concrete["thickness"] for insulator in insulator_rockwool["thickness"]]
aerated_concrete_EPS = [{"aerated_concrete_thickness": brick, "insulator_EPS_thickness": insulator} for brick in
                        aerated_concrete["thickness"] for insulator in insulator_EPS["thickness"]]

hempcrete_rockwool = [{"hempcrete_thickness": brick, "insulator_rockwool_thickness": insulator} for brick in
                      hempcrete["thickness"] for insulator in insulator_rockwool["thickness"]]
hempcrete_EPS = [{"hempcrete_thickness": brick, "insulator_EPS_thickness": insulator} for brick in
                 hempcrete["thickness"] for insulator in insulator_EPS["thickness"]]

# Obtaining the list of materials that meet the requierements of thermal resistance (R-value) without insulator layer:
brick_meet = []
for thickness in brick["thickness"]:
    if thickness * 10 ** -3 / brick["thermal_conductivity"] >= 3.3:
        brick_meet.append(thickness)
    else:
        print('No brick meet')

aerated_concrete_meet = []
for thickness in aerated_concrete["thickness"]:
    if thickness * 10 ** -3 / aerated_concrete["thermal_conductivity"] >= 3.3:
        aerated_concrete_meet.append(thickness)
    else:
        print('No aerated concrete meet')

hempcrete_meet = []
for thickness in hempcrete["thickness"]:
    if thickness * 10 ** -3 / hempcrete["thermal_conductivity"] >= 3.3:
        hempcrete_meet.append(thickness)
    else:
        print('No hempcrete meet')

print("For brick the thicknesses that meet R-reqiurements are:", brick_meet)
print("For aerated_concrete the thicknesses that meet R-reqiurements are:", aerated_concrete_meet)
print("For hempcrete the thicknesses that meet R-reqiurements are:", hempcrete_meet)

# Obtaining the R-value (thermal resistance value), mass and cost values for all aasemblies:
for index, element in enumerate(brick_rockwool):
    brick_rockwool[index]['R-value'] = round(
        element["brick_thickness"] * 10 ** -3 / brick["thermal_conductivity"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 / insulator_rockwool["thermal_conductivity"], 2)
    brick_rockwool[index]['mass'] = round(
        element["brick_thickness"] * 10 ** -3 * brick["density"] + element["insulator_rockwool_thickness"] * 10 ** -3 *
        insulator_rockwool["density"], 2)
    brick_rockwool[index]['cost'] = round(
        element["brick_thickness"] * 10 ** -3 * brick["cost"] + element["insulator_rockwool_thickness"] * 10 ** -3 *
        insulator_rockwool["cost"], 2)

for index, element in enumerate(brick_EPS):
    brick_EPS[index]['R-value'] = round(element["brick_thickness"] * 10 ** -3 / brick["thermal_conductivity"] + element[
        "insulator_EPS_thickness"] * 10 ** -3 / insulator_EPS["thermal_conductivity"], 2)
    brick_EPS[index]['mass'] = round(
        element["brick_thickness"] * 10 ** -3 * brick["density"] + element["insulator_EPS_thickness"] * 10 ** -3 *
        insulator_EPS["density"], 2)
    brick_EPS[index]['cost'] = round(
        element["brick_thickness"] * 10 ** -3 * brick["cost"] + element["insulator_EPS_thickness"] * 10 ** -3 *
        insulator_EPS["cost"], 2)

for index, element in enumerate(aerated_concrete_rockwool):
    aerated_concrete_rockwool[index]['R-value'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 / aerated_concrete["thermal_conductivity"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 / insulator_rockwool["thermal_conductivity"], 2)
    aerated_concrete_rockwool[index]['mass'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 * aerated_concrete["density"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 * insulator_rockwool["density"], 2)
    aerated_concrete_rockwool[index]['cost'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 * aerated_concrete["cost"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 * insulator_rockwool["cost"], 2)

for index, element in enumerate(aerated_concrete_EPS):
    aerated_concrete_EPS[index]['R-value'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 / aerated_concrete["thermal_conductivity"] + element[
            "insulator_EPS_thickness"] * 10 ** -3 / insulator_EPS["thermal_conductivity"], 2)
    aerated_concrete_EPS[index]['mass'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 * aerated_concrete["density"] + element[
            "insulator_EPS_thickness"] * 10 ** -3 * insulator_EPS["density"], 2)
    aerated_concrete_EPS[index]['cost'] = round(
        element["aerated_concrete_thickness"] * 10 ** -3 * aerated_concrete["cost"] + element[
            "insulator_EPS_thickness"] * 10 ** -3 * insulator_EPS["cost"], 2)

for index, element in enumerate(hempcrete_rockwool):
    hempcrete_rockwool[index]['R-value'] = round(
        element["hempcrete_thickness"] * 10 ** -3 / hempcrete["thermal_conductivity"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 / insulator_rockwool["thermal_conductivity"], 2)
    hempcrete_rockwool[index]['mass'] = round(
        element["hempcrete_thickness"] * 10 ** -3 * hempcrete["density"] + element[
            "insulator_rockwool_thickness"] * 10 ** -3 * insulator_rockwool["density"], 2)
    hempcrete_rockwool[index]['cost'] = round(element["hempcrete_thickness"] * 10 ** -3 * hempcrete["cost"] + element[
        "insulator_rockwool_thickness"] * 10 ** -3 * insulator_rockwool["cost"], 2)

for index, element in enumerate(hempcrete_EPS):
    hempcrete_EPS[index]['R-value'] = round(
        element["hempcrete_thickness"] * 10 ** -3 / hempcrete["thermal_conductivity"] + element[
            "insulator_EPS_thickness"] * 10 ** -3 / insulator_EPS["thermal_conductivity"], 2)
    hempcrete_EPS[index]['mass'] = round(element["hempcrete_thickness"] * 10 ** -3 * hempcrete["density"] + element[
        "insulator_EPS_thickness"] * 10 ** -3 * insulator_EPS["density"], 2)
    hempcrete_EPS[index]['cost'] = round(
        element["hempcrete_thickness"] * 10 ** -3 * hempcrete["cost"] + element["insulator_EPS_thickness"] * 10 ** -3 *
        insulator_EPS["cost"], 2)

# Obtaining the list of assemblies that meet the requierements of thermal resistance (R-value):
brick_rockwool_meet = []
for i in brick_rockwool:
    if i['R-value'] >= 3.3:
        brick_rockwool_meet.append(i)
    else:
        pass

brick_EPS_meet = []
for i in brick_EPS:
    if i['R-value'] >= 3.3:
        brick_EPS_meet.append(i)
    else:
        pass

aerated_concrete_rockwool_meet = []
for i in aerated_concrete_rockwool:
    if i['R-value'] >= 3.3:
        aerated_concrete_rockwool_meet.append(i)
    else:
        pass

aerated_concrete_EPS_meet = []
for i in aerated_concrete_EPS:
    if i['R-value'] >= 3.3:
        aerated_concrete_EPS_meet.append(i)
    else:
        pass

hempcrete_rockwool_meet = []
for i in hempcrete_rockwool:
    if i['R-value'] >= 3.3:
        hempcrete_rockwool_meet.append(i)
    else:
        pass

hempcrete_EPS_meet = []
for i in hempcrete_EPS:
    if i['R-value'] >= 3.3:
        hempcrete_EPS_meet.append(i)
    else:
        pass
# Obtaining the the R-value (thermal resistance value), mass and cost values for materials, that meet requierements:
aerated_concrete_meet = []
for thickness in aerated_concrete["thickness"]:
    if thickness * 10 ** -3 / aerated_concrete["thermal_conductivity"] >= 3.3:
        aerated_concrete_meet.append({"aerated_concrete_thickness": thickness, "insulator_thickness": 0,
                                      'R-value': round(
                                          (thickness * 10 ** -3 / aerated_concrete["thermal_conductivity"]), 2),
                                      'mass': round((thickness * 10 ** -3 * aerated_concrete["density"]), 2),
                                      'cost': round((thickness * 10 ** -3 * aerated_concrete["cost"]), 2)})
    else:
        pass

hempcrete_meet = []
for thickness in hempcrete["thickness"]:
    if thickness * 10 ** -3 / hempcrete["thermal_conductivity"] >= 3.3:
        hempcrete_meet.append({"hempcrete_thickness": thickness, "insulator_thickness": 0,
                               'R-value': round((thickness * 10 ** -3 / hempcrete["thermal_conductivity"]), 2),
                               'mass': round((thickness * 10 ** -3 * hempcrete["density"]), 2),
                               'cost': round((thickness * 10 ** -3 * hempcrete["cost"]), 2)})
    else:
        pass

# Aggregating the materials and assemblies which meet requierements into one list:
general_meet = list(aerated_concrete_meet) + list(hempcrete_meet) + list(brick_rockwool_meet) + list(
    brick_EPS_meet) + list(aerated_concrete_rockwool_meet) + list(aerated_concrete_EPS_meet) + list(
    hempcrete_rockwool_meet) + list(hempcrete_EPS_meet)
list(general_meet)
min_R_value = min(i["R-value"] for i in general_meet)
print(min_R_value)
print('General meet: ', general_meet)