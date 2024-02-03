# pyramic triangle
# forRow = int(input('Enter number to make pyramic'))
# spaceRow = forRow
# for i in range(1,forRow):
#     for j in range(spaceRow):
#         print(end=' ')
#     spaceRow = spaceRow-1
#     for k in range(1,i*2):
#         print('*',end='')
#     print('')

# reverse pyramic triangle
forRow = int(input('Enter number to make reverse pyramic'))
forStar = forRow
for i in range(1,forRow):
    for j in range(i):
        print(' ',end='')
    for k in range((forStar*2),3,-1):
        print('*',end='')
    forStar = forStar-1
    print(' ')