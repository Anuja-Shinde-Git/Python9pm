info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}

# info2 = info
# info2['age'] = 89

# print(info)
# print(info2)

# copy()
info3 = info.copy()
info3['age'] = 55
print(info)
print(info3)

# program 2
# clear()
info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}
# info.clear()
# print(info)

# pop(key)
# info.pop('age')
# print(info)

# #popitem()
# info.popitem()
# print(info)

# update()
# info.update({"city":"pune","language":"hindi"})
# print(info)

# program 3

info = {
    "first_name":"chinmay",
    "last_name":"deshpande",
    "age":10,
    "rollNo":45
}

# get()
#q11 = info['Age']
q1 = info.get('Age')
print(q1)
# print(q11)
print("hello")

# loop 

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}

print(vehicle['color'])
for item in vehicle:
    print(item,vehicle[item])

for x in vehicle.keys():
    print(x)

for y in vehicle.values():
    print(y)

for k,v  in vehicle.items():
    print(k , v)




# info2 = {
#     "firstName":"chinmay",
#     "lastName":"deshpande"
# }
# info2.clear()
# info2.copy()
# info2.pop('firstName')
# info2.popitem()
# info2.update({"city":"pune"})

# # for key in info2:
# #     print(key , info2[key])

# for key in info2.keys():
#     print(key)
# for val in info2.values():
#     print(val)
# for k,v in info2.items():
#     print(item)
#info2.get("firstName")

# program 1
e = dict.fromkeys(["amol","chinmay","ram"])
print(e)

info3 = {
    "admin":"chinmay",
    "customer":"sameer",
    "support":"raj"
}

info3.setdefault("manager",None)
print(info3)

# fromkeys()
f = dict.fromkeys(["key1","key2","key3"])
print(f)


# tuple vs list

listName = ["amol","chinmay","ram"]
print(listName)
print(type(listName))
listName.append("raj")
print(listName)
listName[0] = "sarika"


listNameB = ("amol","ram","satish")
print(listNameB)
print(type(listNameB))
#listNameB[0] = "sam"


# program 2

tupleB = (11,22)
tupleA = ("chinmay","raaj")
tupleC = (["ninad","vijeet"],["rohit","ameya"])
tupleD = 11,12
print(type(tupleD))


# program 3 
names = ("sonal","sham","ram")
print(names[0])
print(names[1])
print(names[2])

# using range 

for x in range(len(names)):
    #print(x)
    print(names[x])

# without using range
for item in names:
    print(item)

#program 4
    
tupleD = (11,22,33,44,55,66,33,55,33)
q = tupleD.count(33)
print(q)

w = tupleD.index(22)
print(w)