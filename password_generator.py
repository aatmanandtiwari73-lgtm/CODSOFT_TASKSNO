import random
import string

def generate_password():
    print("--- PASSWORD GENERATOR ---")
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
    except ValueError:
        print("Please enter a valid integer for length.")
        return

    print("\nSelect Password Complexity:")
    print("1. Letters only (Uppercase & Lowercase)")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Special Symbols (Strong)")
    
    complexity = input("Enter choice (1/2/3): ").strip()

    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice! Defaulting to Strong complexity.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    generate_password()
