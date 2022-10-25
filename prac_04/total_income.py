"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month_number in range(1, months + 1):
        # income = float(input("Enter income for month " + str(month_number) + ": "))
        income = float(input(f"Enter income for month {months}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month_number in range(len(incomes)):
        income = incomes[month_number - 1]
        total += income
        # print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_number, income, total))
        print(f"Month {month_number:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()