import json

diction = {1:1, 2:2}

print(diction)
print(type(diction))

diction = json.dumps(diction)

print(diction)
print(type(diction))

diction = json.loads(diction)

print(diction)
print(type(diction))