# Special Operators . . 
#  1.Identity Operator
#  - is , is not (memory location)
#  2.Membership Operator

# a = 10
# b = 20
# c = a is b  
# print('memory location using is word : ', c)

p = 10
t = 10
# if p is t:
#     print('They are same location')
# else:
#     print('The are not the same location')
# p = 20
# if p is t:
#     print('second time, They are same location')
# else:
#     print(' second time, They are not the same location')

# if p is not t:
#     print('they are not the same location')
# else:
#     print('they are same location')

###### checking type by using is keyword

w = type(p) is int
# print('type() by is ', w)

r = type(p) is not int
# print('type() check by is not', r)

y = type(p) is float
# print('type() check by is for float',y)


# String check

u = 'Pyae Phyo Thant'
o = 'Pyae Phyo Thant'
# print(id(u),id(o))
e = u is o
# print('e',e)

# if u is o:
    # print('they are same location')
# else:
    # print('they are not the same location')

# Membership
#  - in , not in

mylist = ["apple", "banana", "cherry"]
checkItem = "banana" in mylist
# print('check item has or not', checkItem)
checkItem2 = "banana" not in mylist
# print('check item not has', checkItem2)
# def pver():
#     return 0
# print('return 0', pver())

pptList1 = [1,2,3,4,5]
pptList2 = [6,7,8,9]

def overLap(pptList1,pptList2):
    p = 0
    t = 0
    for i in pptList1:
        p+=1
    for i in pptList2:
        t+=1
    for i in range(0,p):
        for j in range(0,t):
            if pptList1[i] == pptList2[j]:
                return 1
    return 0
    
# Notes => if the return value is 0 => falsy!!!!
if overLap(pptList1,pptList2):
    print(overLap(pptList1,pptList2))
else:
    print('____________________')