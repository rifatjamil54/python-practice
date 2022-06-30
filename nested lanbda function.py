add = lambda x = 10 : (lambda y : x + y)

a = add(4)

print(a(5))