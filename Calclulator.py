
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))

            if choice in (1, 2, 3, 4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    print("Result:", add(num1, num2))
                elif choice == 2:
                    print("Result:", subtract(num1, num2))
                elif choice == 3:
                    print("Result:", multiply(num1, num2))
                elif choice == 4:
                    result = divide(num1, num2)
                    print("Result:", result)
                
                break
            else:
                print("Invalid input. Please choose a valid operation (1/2/3/4).")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
