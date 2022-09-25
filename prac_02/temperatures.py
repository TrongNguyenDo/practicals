def main():
    celsius = float(input("Celsius: "))
    fahrenheit = float(input("Fahrenheit: "))

    celsius12 = cel_to(celsius)
    print(celsius12)

    fahrenheit12 = fa_to(fahrenheit)
    print(fahrenheit12)


def cel_to(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fa_to(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
