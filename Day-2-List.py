boys =['maruf','sayem','rakib','eaysin']
# print(boys.title()) >>THIS IS INVALID.RETURN ERROR
# print(boys[1].title())
# print(boys[3].upper())
# print(boys[0])

# messge = f"My first frined was {boys[3].upper()}"
# print(messge) --.. this is important

# MODIFING ELEMENTS IN A LIST..
# print(boys)
# boys[0] = "shuvo"
# print(boys)

# APPENDINING ELEMENTS -->>
# print(boys)
# boys.append("asif")
# print(boys)

# girls = []
# girls.append("ayat")
# girls.append("nova")
# girls.append("tisha")
# # print(girls.title()) -->>return err0r
# print(girls)

# INSERTING ELEMENTS ->>
# print(boys)
# boys.insert(1,"tarikul")
# print(boys)

# removing elements-->>
# print(boys)
# del boys[1]
# print(boys)

# popped methods-->>
print(boys)
popped_boy = boys.pop()
print(boys)
print(popped_boy.title())