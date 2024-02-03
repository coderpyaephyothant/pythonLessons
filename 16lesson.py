# Memory address
p = 10
e = 10

t = id(p)
y = hex(p)

w = id(e)
v = hex(e)

# print(p)
# print(t)   #decimal value
# print(y)   #hex value
# print(v)
# print(w)

if t == w :
    print('Same Memory',t,w)
else:
    print('Different memory allocation',t,w)


