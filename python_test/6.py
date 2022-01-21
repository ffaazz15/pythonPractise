car = {
    "brand" : "mercedes",
    "color": "blue",
    "year" : 2022 ,
    "model": "s class"
}
x = car.keys()
print(x)     #before change the catch is we requre keys 

car["tyre"] = "mrf"
print(x)  #after change


#lets remove an item
car.pop("model")
print(car)

for x in car:
    print(x)

#other way for a for loop is 
for x in car.keys():
    print(x)

    