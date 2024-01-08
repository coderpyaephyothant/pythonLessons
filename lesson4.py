# control structures
a = 400
b = 300
# if a < b :
#     # print('a less than b')
# else :
#     # print('b greater than a')


c = 500
d = 500
# if c < d:
#     # print('c less than d')
# elif c > d:
#     # print('c greater than d')
# else :
#     # print('c and d value are equal')

# largest Number
a = 100
b = 200
c = 300
d = 400

if (a > b) and (a > c) and (a > d) : 
    largestNumber  = a 
    print('Largest Number is : ', largestNumber)
elif (b > a ) and ( b > c) and (b > d) : 
    largestNumber = b
    print('largest Number is : ', b)
elif (c > a) and (c > b) and (c > d):
    largestNumber = c
    print('largest Number is : ', largestNumber)
else :
    largestNumber = d
    print('largest Number is : ', largestNumber)
 
