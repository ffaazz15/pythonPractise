
class Dog:
	
	# A simple class
	# attribute
	attr1 = "dog"
	attr2 = "really happy"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
tommy= Dog()

# Accessing class attributes
# and method through objects
print(tommy.attr1)
tommy.fun()
