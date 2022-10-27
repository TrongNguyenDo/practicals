from guitar import Guitar

THIS_YEAR = 2022

name = "Gibson L-5 CES"
year = 1922

guitar = Guitar(name, year)
other_guitar = Guitar("Another Guitar", 2013)
print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected {9}. Got {other_guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage() - Expected {False}. Got {other_guitar.is_vintage()}")

