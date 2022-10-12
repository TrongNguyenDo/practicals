def main():
    # lindsay.ward@jcu.edu.au
    email = input("Please enter your email: ")
    email_name = {}
    while email != "":
        get_name = extract_name(email)
        confirmation = input(f"Is your name {get_name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            get_name = input("Name: ")
        extract_name(email)[email] = get_name
        email = input("Email: ")

    for email, get_name in extract_name(email).items():
        print(f"{get_name} ({email})")


def extract_name(email):
    change = email.split('@')[0]
    new_change = change.split('.')
    get_name = " ".join(new_change).title()
    return get_name


main()
