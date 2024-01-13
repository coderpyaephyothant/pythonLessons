# lottery game
import secrets
secureNumber = secrets.SystemRandom()
# build object
# print(secureNumber)

while True:
    print('_________Welcome to 2D game with Python Programming_________')
    # exit()
    press1 = int(input('______Press 1 for RULES OR 2 to start Game!____'))
    if press1 == 1:
        print(' >Your Age must be greater than or equal 17! ')
        print(' >You need aleast 10000 Coin! ')
        print(' >Your need to use aleast 1000 Coin to start game! ')
    if press1 == 2:
        print(' >You can start to play game Now! -----------')
        print(' > Now, You need to fill some of your informations...')
        print('Lets Start!')
        clientName = input('Type your name : at least 3 words')
        clientAge = int(input('Type your age : at least 17year!'))
        if len(clientName) < 3:
            print('Your Name must be aleast 3Characters!')
        if clientAge < 17:
            print('Your Age must be aleast 17!')
            exit()
        if len(clientName) > 3 and clientAge >= 17:
            print('You can play game Now. ...')
            print('Welcome', clientName ,'!. . ')
            clientMoney = int(input('Now, Enter your coin! : aleast 10000 Coin'))
            while clientMoney < 10000 or None:
                print('Coin must be aleast 10000!', clientName, 'coin is', clientMoney )
                clientMoney =  int(input('Please valid coin!'))
                if clientMoney < 10000:
                    continue
            if clientMoney >= 10000:
                print('Hello', clientName, 'Thanks You! - - - -')
                clientUseMoney = int(input('How many conin wanna use ? Enter. :aleast 1000 : '))
                while clientUseMoney < 1000 or None:
                    print('Use Coin must be aleast 1000!', clientName, 'Used coin is : ', clientUseMoney )
                    clientUseMoney =  int(input('Please valid Use coin!'))
                    if clientUseMoney < 1000:
                        continue   
                if clientUseMoney >= 1000:
                    print('You used ', clientUseMoney , 'coin for game!- - -')
                    luckyNum = int(input('Insert your lucky Number! Must be two Number!------ '))
                    while len(str(luckyNum)) < 2 or None:
                        print('Use two number!', clientName, 'inserted lucky number is', luckyNum )
                        luckyNum =  int(input('Please valid Luck Number!'))
                        while len(str(luckyNum)) < 2 or len(str(luckyNum)) > 2:
                            continue 
                    if len(str(luckyNum)) == 2:
                        sysNumber = secureNumber.randint(10,99)
                        countNum = 0
                        while countNum < 3:
                            print('Wait... What is Number Today is . . .')
                            countNum +=1
                        if sysNumber == luckyNum:
                            clientMoney = clientMoney + clientUseMoney
                            print('Today Number is : ', sysNumber)  
                            print('Hey',clientName,'Congratulation. . .You Won!!!!----')
                            print('Hey',clientName,'You got',clientMoney)
                        else:
                            clientMoney = clientMoney - clientUseMoney
                            print("Today number is :", sysNumber)
                            print("Your Lucky number is :", luckyNum)
                            print("Sorry..Good Luck again", clientName)
                            print('Hey',clientName,'Your Coin : ',clientMoney)
    print('Your Coin',clientMoney)
                        
                        



        
    