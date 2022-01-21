list = ["apple" , "banana" , "mango"]
# list.append("orange")
# print(list)


tropicalFruits =  ["papaya" , "pineapple"]
list.extend(tropicalFruits)
print(list)
list.remove("apple")
print(list)
list.pop(2)
print(list)


i = 0 
while  i < len(list):
    print(list[i])
    i = i+1
