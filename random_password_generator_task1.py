
import secrets
import string


def generate_password():
    print("===== RANDOM PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length < 1:
            print("Password length must be at least 1.")
            return

        print("\nChoose character types:")
        print("1. Lowercase letters (a-z)")
        print("2. Uppercase letters (A-Z)")
        print("3. Numbers (0-9)")
        print("4. Special characters (!@#$...)")

        choices = input(
            "Enter your choices (e.g. 1234): "
        )

        characters = ""
        password = []

        if "1" in choices:
            characters += string.ascii_lowercase
            password.append(secrets.choice(string.ascii_lowercase))

        if "2" in choices:
            characters += string.ascii_uppercase
            password.append(secrets.choice(string.ascii_uppercase))

        if "3" in choices:
            characters += string.digits
            password.append(secrets.choice(string.digits))

        if "4" in choices:
            characters += string.punctuation
            password.append(secrets.choice(string.punctuation))

        if not characters:
            print("Please select at least one character type.")
            return

        if len(password) > length:
            print("Password length is too short for selected choices.")
            return

        while len(password) < length:
            password.append(secrets.choice(characters))

        secrets.SystemRandom().shuffle(password)

        print("\nYour generated password is:")
        print("".join(password))

    except ValueError:
        print("Please enter a valid number for password length.")


if __name__ == "__main__":
    generate_password()
