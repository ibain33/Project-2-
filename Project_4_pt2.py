import random

random_numbers = [ ]


while len(random_numbers) < 50:
    random_numbers.append(random.randint(1, 100))

print("List of random numbers:")

print(random_numbers)

count_between_71_79 = 0

highest_number = random_numbers[0] 
lowest_number = random_numbers[0]   


for num in random_numbers:
    if num >= 71 and num <= 79:
        count_between_71_79 += 1
    if num > highest_number:
        highest_number = num
    if num < lowest_number:
        lowest_number = num

print("Generated Numbers:", random_numbers)
print("\nCount of numbers between 71 and 79 inclusive:", count_between_71_79)
print("Highest number in the list:", highest_number)
print("Lowest number in the list:", lowest_number)
