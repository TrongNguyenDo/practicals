import random


def main():
    number_pick = int(input("How many quick picks ? "))
    check_input(number_pick)
    random_numbers(number_pick)


def check_input(number_pick):
    valid_input = False
    while not valid_input:
        try:
            if number_pick <= 0:
                print("Wrong input!")
                number_pick = int(input("How many quick picks ? "))
            else:
                valid_input = True
                return number_pick
        except ValueError:
            print("Invalid input!")


def random_numbers(number_pick):
    for i in range(number_pick):
        quick_pick = []
        for j in range(6):
            number = random.randint(1, 45)
            while number in quick_pick:
                number = random.randint(1, 45)
            quick_pick.append(number)
        quick_pick.sort()
        # List comprehension
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()