# Secure random
import secrets

# secrets.SystemRandom

# randint & randint
# secureGenerator = secrets.SystemRandom()
# secureRandNumber = secureGenerator.randint(2,10)
# print('secured random numbers', secureRandNumber)

# secureGenerator = secrets.SystemRandom()
# secureRandNumberByRange = secureGenerator.randrange(2,11,4)
# ရွေးချယ်ခွင့် တိုးပွားမှုကို သတ်မှတ်သည့် ကိန်းပြည့်။ default 1
# print('secured random numbers ranges', secureRandNumberByRange)

# choice & sample
# fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry']
# secureGenerator = secrets.SystemRandom()
# secureFruit = secureGenerator.choice(fruits)
# print('securedFruit', secureFruit)

# secureGenerator = secrets.SystemRandom()
# secureFruitSample = secureGenerator.sample(fruits,2)
# print('secureFruitSample', secureFruitSample)

# secret.token_byte
# print(secrets.token_bytes(4))
# print(secrets.token_bytes(2))
# secret.token_hex 2 => 4 , 4 => 8
# print(secrets.token_hex(3)) 

# Token URL safe
# print(secrets.token_urlsafe(2))

passwordResetLink = 'http://resetUrlLink/reset='
passwordResetLink += secrets.token_urlsafe()
print('url secretlinks', passwordResetLink)

