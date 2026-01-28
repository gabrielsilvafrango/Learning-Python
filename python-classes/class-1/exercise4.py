def print_menu():
    print("Menu:")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def sum():
    print("You chose Sum")
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    print("The result is:", value1 + value2)

def sub():
    print("You chose Subtraction")
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    print("The result is:", value1 - value2)

def mult():
    print("You chose Multiplication")
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    print("The result is:", value1 * value2)

def div():
    print("You chose Division")
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    print("The result is:", value1 / value2)

print_menu()

option = input("Choose an option: ")

if option == "1":
    sum()
elif option == "2":
    sub()
elif option == "3":
    mult()
elif option == "4":
    div()
else:
    print("Invalid option")