try:
    raise NameError("hi thre")
except NameError:
    print("An Exception")
    raise