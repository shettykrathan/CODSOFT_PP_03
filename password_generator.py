
import random
import string

def create_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            user_length = int(input("Enter the desired length of your password: "))
            if user_length < 4:
                print("Try something longer for better security (at least 4 characters).")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    generated = create_password(user_length)
    print("\nHere is your generated password:")
    print(generated)

if __name__ == "__main__":
    main()
