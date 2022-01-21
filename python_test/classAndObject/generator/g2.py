def simpleGenerator():
    yield 1 
    yield 2
    yield 3

x = simpleGenerator()
print(x.next())
print(x.next())
print(x.next())