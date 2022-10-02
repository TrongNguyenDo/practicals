"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
.Answer: When you enter a wrong type of input.
2. When will a ZeroDivisionError occur?
.Answer: When you enter your  denominator as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
.Answer: Yes ,i could
"""
value_check = False
while not value_check:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        if denominator == 0:
            denominator = int(input("Enter the denominator: "))
        else:
            value_check = True
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
