class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return a / b


calc = Calculator()
print("Welcome to Simple Calculator")

while True:
    # taking input
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    # menu
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Try again.")
        continue

    if ch == 0:
        print("Exiting...")
        break
    elif ch == 1:
        print("Result:", calc.add(a, b))
    elif ch == 2:
        print("Result:", calc.subtract(a, b))
    elif ch == 3:
        print("Result:", calc.multiply(a, b))
    elif ch == 4:
        result = calc.divide(a, b)
        if result is not None:
            print("Result:", result)
    else:
        print("Wrong choice, try again.")
