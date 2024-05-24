import random # import a library that will allow us to generate random numbers
import math

#part1 Random number cubed 

random_number = random.randint(1,6) 
random_number_cubed = random_number ** 3
print ("Part 1")
print (random_number) 

#paart2 Random number with squareroot 

random_number = random.randint(11,99) 
random_number_sqrt = math.sqrt(random_number)
print("Part 2")
print (random_number)

#part3 Random number diplayed right to left

random_number = random.randint(17500,82228)
print ("Part 3")
print (random_number) 

while random_number > 0:
    digit = random_number % 10
    print(digit)
    random_number //= 10
 
