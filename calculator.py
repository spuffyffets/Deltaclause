def main():
  # Function for the calculator
  while True:
    # Get user input
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      operation = input("Enter an operation (+, -, *, /): ")
    except ValueError:
      print("Invalid input. Please enter numbers and a valid operator.")
      continue

    # Perform calculation based on user choice
    if operation == "+":
      result = num1 + num2
      print(f"{num1} + {num2} = {result}")
    elif operation == "-":
      result = num1 - num2
      print(f"{num1} - {num2} = {result}")
    elif operation == "*":
      result = num1 * num2
      print(f"{num1} * {num2} = {result}")
    elif operation == "/":
      if num2 == 0:
        print("Error: Division by zero is not allowed.")
      else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
      print("Invalid operation. Please enter +, -, *, or /.")

    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (y/n): ").lower()
    if choice != 'y':
      break

if __name__ == "__main__":
  main()
