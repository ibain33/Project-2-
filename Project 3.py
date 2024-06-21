def calculate_skill_level(average):
    if average < 100:
        return "Beginner"
    elif average < 150:
        return "Intermediate"
    else:
        return "Advanced"

def main():
    # collect user info and create username
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")

    username = (first_name[0] + last_name + age).lower()

    # input bowling scores
    scores = []
    for i in range(3):
        while True:
            try:
                score = int(input(f"Enter score {i+1} (0-300): "))
                if score < 0 or score > 300:
                    print("Invalid score! Please enter a score between 0 and 300.")
                    continue
                scores.append(score)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer score.")

    # average scores and determine skill level
    average = sum(scores) / len(scores)
    skill_level = calculate_skill_level(average)

    # output results and print formatted output
    full_name = f"{first_name} {last_name}"
    print(f"\nThanks for playing {full_name}! Your username is {username}, your average score is {average:.0f}, "
          f"and your skill level is {skill_level}.")
    print("Good Job! Keep working hard!")

if __name__ == "__main__":
    main()
