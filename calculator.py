def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("=== Simple Calculator ===")
    print("Operations: add, sub, mul, div")
    
    while True:
        op = input("\nEnter operation (add/sub/mul/div or quit): ").lower()
        if op == 'quit':
            print("Exiting calculator.")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if op == 'add':
            print(f"Result: {add(a, b)}")
        elif op == 'sub':
            print(f"Result: {subtract(a, b)}")
        elif op == 'mul':
            print(f"Result: {multiply(a, b)}")
        elif op == 'div':
            print(f"Result: {divide(a, b)}")
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()
