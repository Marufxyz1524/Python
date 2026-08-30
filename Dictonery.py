# BASIC BEFORE LEARN DICTIONERY
# student = dict(name="Rahim", age=20, cgpa=3.75)
# student = {"name" : "Rahim","Roll":34}

# Nicher ta best-->>
# student = {}
# student["name"] = "Nishat"
# student["age"] = 34
# student["hometown"] = "Rangpur"
# print(student)

# info = {
#     "name": "Maruf",
#     "varsity" : "Daffodil",
#     "Roll" : 34
# }
# # how to adding/removing

# info["name"] = "Nishat"  #removing
# info["surname"] = "Billah"
# print(info)

##MODIFYING DICT
items = {}
items['st1'] = "Rice"
items['st2'] = 'Pizza'
items['st3'] =' Burger'
print(items)

## modiyng

# items = {'st2' : 'Noodles'}
# print(f"Now the menu is {items['st2']}")

## deleting
# del items['st2']
# print(items)

# loop throw
for item , name in items.items():
    print(f"\nItem : {item}")
    print(f"Name : {name} ")