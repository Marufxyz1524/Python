##kono file er vitor ki ache seta ki vabe print korbo:

# with open("sample.txt","r") as file:
#     sample = file.read()
# print(sample)    

## purono data rekhe notun kichi likhbe

with open("sample.txt","a") as file:
    file.write("\nI am future Billionere ")

with open("sample.txt","r") as file:
    data = file.read()
print(data)    

