
def main():

    operation = input("type of operation: ")
    num1 = int(input("enter your first number for op: "))
    num2 = int(input("enter second number: "))

    if operation == "-":
        total = num1 - num2
    elif operation == "+":
        total = num1 + num2
    elif operation == "*":
        total = num1 * num2
    elif operation == "/":
        total = num1 / num2
    else:
        print(" ")
    print(int(total))


if __name__ == "__main__":
    main()
