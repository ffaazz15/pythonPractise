def simpleGenerator():
    yield 2
    yield 3

for value in simpleGenerator():
    print(value)