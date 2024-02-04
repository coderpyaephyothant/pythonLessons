# Logical Operators
# p = True
# print('not p value is : ', not p)

# Lesson18
# Bitwise Operators
#       Bitwise operators are used to compare (binary) numbers:

# Bitwise AND
a = 60
b = 13
c = 0
c = a & b
# print('bitwise and operation', c)

#    60 /2 & 13/2 ,    2|60 - 0                     2|13 -1
#                  2|30 - 0                      2|6 - 0
#                     2|15 - 1                    2|3 -1 
#                        2|7 - 1                   2|1
#                          2|3 - 1
#                            2|1
                            # 1 1 1 1 0 0           # 1 1 0 1
                            # 0 0 1 1 0 1    
        #    Ans Bitwise &       0 0 0 0 1 1 0 0  = 12


# Bitwise OR
e = 60
f = 13
g = 0
g = e | f
# print('bitwise or operation', g)

#                   111100
#                   001101
# Ans Bitwise |          00111101 = 61


# Bitwise Nor
a = ~ 10
# print('Bitwise Nor', a)
# format => - (num + 1 )

# decimal to binary      2|10 - 0
                        #    2|5 - 1
                            # 2|2 -0
                            #   2|1 
                            #  1010 (need to add 1)
                            #  -(1011)

# Two's complement
# 10 => 1010
#   inverse => 0101 
#    plus one =>       0110
#  and then change plus to minus , minus to plus






