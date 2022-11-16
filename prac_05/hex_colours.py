CODE_TO_COLOR = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "aqua": "#00ffff",
    "army green": "#4b5320",
    "arylide yellow": "#e9d66b",
    "ash grey": "#b2beb5",
}

print(CODE_TO_COLOR)
code_color = input("Enter the color: ").lower()
while code_color != "":
    if code_color in CODE_TO_COLOR:
        print(code_color, "is", CODE_TO_COLOR[code_color])
    else:
        print("Invalid short state")
    code_color = input("Enter short state: ").lower()
print("Bye")