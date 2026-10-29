# Simple Calculator
# Internship Task 1 - CodeOrbit Tech

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = input("\nEnter your choice (1-4): ")

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-4.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operations = {
            "1": ("Addition", add),
            "2": ("Subtraction", subtract),
            "3": ("Multiplication", multiply),
            "4": ("Division", divide)
        }

        operation_name, operation = operations[choice]
        result = operation(num1, num2)

        print(f"\n{operation_name} Result: {result:g}")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    calculator()