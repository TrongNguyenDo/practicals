"""names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove?")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Invalid name!")
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove?")
print("Thank you for using the program!")
"""


def main():
    n = int(input("Enter the number u want to use ?"))
    lst = []
    for i in range(n):
        lst.append(int(input("This is the numbers in the list")))
    nathan = sum_numbers_larger_average(lst)
    print(nathan)


def sum_numbers_larger_average(lst):

    average = sum(lst)/len(lst)
    result = 0
    if all(number <= average for number in lst):
        return -1
    for i in lst:
        if i > average:
            result += i
    return result


main()
