# Function definitions for basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Main calculator logic
def calculator():
    print("Welcome to the Command-Line Calculator!")
    
    while True:
        print("\nSelect Operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'

            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please select from 1 to 5.")

# Run the calculator
if __name__ == "__main__":
    calculator()
