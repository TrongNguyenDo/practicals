import random


def main():
    score = float(input("Enter score: "))
    new_score = todo(score)
    print(new_score)
    # Generate random number and give the score result base on the random number
    score2 = random.random()
    new_score1 = todo(score2)
    print("Random number generate:", score2)
    print("Random number generate gives result:", new_score1)


def todo(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Bye"


main()
