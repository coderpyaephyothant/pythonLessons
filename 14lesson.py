# string with for loop
# words = 'pyaephyothant'
# for x in words:
#     print(x, end='-')
# with index
# i = 0
# for x in words:
#     print(i,x)
#     i+=1
# enumerate
# for i,x in enumerate(words):
#     print(i,x)

# row = int(input('write number between 1 and 5'))
# for p in range(row):
#     for t in range(p):
#         print('*',t,'t')
#     print('-',p,'p')


# row = int(input('write number between 1 and 10'))
# for p in range(row):
#     for t in range(p):
#         print(t,end='')
#     print('-')

# for p in range(1,row):
#     # print(p,'p')
#     for t in range(p):
#         print(t,end='')
#     print('-')

# x = range(3, 0, -2)
# print(x)
# for n in x:
#   print(n)

putInNumber = int(input('insert value of a number between 1 and 5 = '))
for p in range(5,putInNumber):
    for t in range(p,0,-1):
        print('t',t)
    print('-')

