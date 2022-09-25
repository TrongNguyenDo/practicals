def main():
    score = int(input("1.Enter your score: "))
    score = input_check(score)
    print("2.Check your result: ")
    score_check(score)
    print("3.Print stars: ")
    stars_print(score)
    print()
    print("4.Quit")
    end_program()


def input_check(score):
    value_score = False
    while not value_score:
        try:
            if score < 0 or score > 100:
                print("Score must be >= 0 and <= 100 !")
                score = int(input("1.Enter your score: "))
            else:
                value_score = True
                return score
        except ValueError:
            print("Invalid score !")
        print("You have entered a correct mark!")


def score_check(score):
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    elif score <= 100:
        print("Excellent")


def stars_print(score):
    for i in range(score):
        print('*', end="")


def end_program():
    print("Thank you for using this program :).Have a nice day!")


main()
