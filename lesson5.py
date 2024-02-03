# calculator program
# Lesson 5 

print("Press + for Add")
print("Press - for Subtract")
print("Press * for Multiply")
print("Press / for Divide")

userInput = input('please enter operator for Add or Subtract or Multiply or Divide')
# print(userInput)
print('you entered : ', userInput)

firstNumber = int(input('Enter Your First Number'))
print('your first number is : ', firstNumber)

secondNumber = int(input('Enter Your Second Number'))
print('your second number is : ', secondNumber)

if userInput == '+' :
    result = firstNumber + secondNumber
    print('result is :', result)
elif userInput == '-' :
    result = firstNumber * secondNumber
    print('result is :', result)
elif userInput == '*' :
    result = firstNumber * secondNumber
    print('result is :', result)
elif userInput == '/' :
    result = firstNumber / secondNumber
    print('result is :', result)
else :
    print('your input {} is invalid ! Please try again later!'.format(userInput) )
    exit()




