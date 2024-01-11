# Random
import random


# The random() method returns a random floating number between 0 and 1.
# print(random.random())

# for integers randint() randrange()
# print(random.randint(2,6))

# random.randrange(start, stop, step)
print(random.randrange(2,8,2))

# random.choice(sequence)
# random.sample(sequence, k) sequence	Required. A sequence. Can be any sequence: list, set, range etc. && k	Required. The size of the returned list
# fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry']
# print(random.choice(fruits))
# print(random.sample(fruits,2))

# random.seed(a, version)
# *** Random.seed is not secure!!!!!!!!!!!!!!!!!!
# a	Optional. The seed value needed to generate a random number.
# If it is an integer it is used directly, if not it has to be converted into an integer.
# Default value is None, and if None, the generator uses the current system time.

# version	An integer specifying how to convert the a parameter into a integer.
# Default value is 2

# random.seed(42)
# print(random.random())

# shuffle
# Shuffle a list (reorganize the order of the list items):
# fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry']
# print('Before Shuffle/ original fruits list', fruits)
# random.shuffle(fruits)
# print('Shuffled List', fruits)

# uniform random.uniform(a, b)
# a	Required. A number specifying the lowest possible outcome
# b	Required. A number specifying the highest possible outcome
# The uniform() method returns a random floating number between the two specified numbers (both included).

# print('uniform', random.uniform(5,10))
# random.triangular(low, high, mode)
# print(random.triangular(20, 60, 10))



