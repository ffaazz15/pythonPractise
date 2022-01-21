# def is_even(n):
#     return n%2 == 0
# by usning lamda u can avoid the above steps

nums = [2,2,3,4,7,8,9]
evens = list(filter(lambda n : n %2 == 0,nums))
doubles =list(map(lambda n : n+2,nums))

print(doubles)
print(evens)
