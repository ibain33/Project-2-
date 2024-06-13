import random
 
#User enter first name
first_name = input("Please enter your first name: ")
 
#User enter last name 
last_name = input("Please enter your last name: ")
 
# Concatenating both names
full_name = first_name + " " + last_name
 
#Print full name
print("Your full name is:", full_name)
 
#Calculate length of full name
name_length = len(full_name)
 
#Print length of full name
print("The length of your full name is:", name_length)
 
#select random number between 0 and length of user name.
random_number = random.randint(0, name_length - 1)
 
#Print character that is selected by random number
 
random_character = full_name[random_number]
 
print("The character at position", random_number, "is:", random_character)
