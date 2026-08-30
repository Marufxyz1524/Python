stdnt = {
    "name" : "Maruf Billah",
    "score" : {          ##this is nested dict
        "phy" : 98,
        "chem": 56,
       "math" : 98
    }
}

# print(stdnt)
# print(stdnt.keys())  ## return all keys
# print(list(stdnt.keys()))
# print(len(list(stdnt.keys())))
# print(stdnt.values()) ##return all values 
# print(stdnt.items())  ## return all key,valus pairs as tuple

## Accessing items in list
# pairs = list(stdnt.items())
# print(pairs[0])

##difference bitween nrml print & .getprint
# print(stdnt["name"])
# print(stdnt.get("name"))
##if we wr8 name2 1stprint return error
## but 2nd print rturn NONE thats the differnce
# print(stdnt["name2"])
# print(stdnt.get("name2"))  ##this is stndrd

##Update dict
new_dict = {"city" : "rangpur","age" : 45}
stdnt.update(new_dict)
print(stdnt)



