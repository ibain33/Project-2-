#User input 3 dfferent bowling scores
score1 = input("Enter the first bowling score: ")
 
score2 = input("Enter the second bowling score: ")
 
score3 = input("Enter the third bowling score: ")
 
#Convert the scores to integers 
scores = [int(score1), int(score2), int(score3)]
 
#Calculate 3 different types of scores
 
#Calculate maximum 
high_score = max(scores)
#Calclate minimum
low_score = min(scores)
#Calculate average
average_score = round(sum(scores) / len(scores))
 
#Print all three scores
 
print("Your High score:", high_score)
 
print("Your Low score:", low_score)
 
print("Your Average score:", average_score)
