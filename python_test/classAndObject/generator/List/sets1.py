from hashlib import new


thisset = {"apple" , "banana" , "cherry"}
print(len(thisset))
thisset.add("orrange")
print(thisset)
print(type(thisset))

newlist = ["kiwi" , "orange"]
thisset.update(newlist)
print(thisset)