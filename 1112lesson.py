yourInput = input('enter your number')
while True:
    if yourInput.isdigit() and len(yourInput) <3:
        print('your input must be atleast 3word')
        break
    elif yourInput.isdigit() and len(yourInput) > 3:
        print('not greater than 3')
    else:
        print('ok')
        break