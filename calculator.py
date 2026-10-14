def calculator():
    print("--- SIMPLE CALCULATOR ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter operation choice (1/2/3/4 or + - * /): ").strip()

    if choice in ('1', '+'):
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")
    elif choice in ('2', '-'):
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")
    elif choice in ('3', '*'):
        print(f"\nResult: {num1} * {num2} = {num1 * num2}")
    elif choice in ('4', '/'):
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            print(f"\nResult: {num1} / {num2} = {num1 / num2}")
    else:
        print("\nInvalid operation choice!")

if __name__ == "__main__":
    calculator()
