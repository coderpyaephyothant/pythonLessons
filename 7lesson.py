# while loop

# i = 1
# while i < 10:
    # print('looping number of i value is : {}'.format(i))
    # i += 1 

# while loop exercise
p = 0
t = 5

# while t > p : 
#     print('p is' , p, 't is' , t)
#     t -=  1

# break and continue

# for pt in 'pathein':
#     if pt == 'n':
#         break
#     print('without break')

# print('----------breaked--------------')


# for pp in 'yangon':
#     if pp == 'n':
#         continue
#     print('without break',pp)
# print('---------continue-----')



# while and break programm
ls = [10,20,60,99]
compareNum = 99
found = False
index = 0 
# print(len(ls))

while index < len(ls):
    if ls[index] == compareNum:
        found = True
        break
    index += 1

if not found:
    # print(not found)
    ls.append(compareNum)

# print(ls)

