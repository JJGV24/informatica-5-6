

def main():

    operation = input("enter your arithmetic operation using spaces between numbers and operator: ")
    parts = operation.split( )

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    total = float(0)

    if operator == "-":
        total = num1 - num2
    elif operator == "+":
        total = num1 + num2
    elif operator == "*":
        total = num1 * num2
    elif operator == "/":
        total = num1 / num2
    else:
        print(" ")

    tiktok = round(total,1)
    print(f"{tiktok}")


    #print(float(num1))
    #print(operator)
    #print(float(num2))

if __name__ == "__main__":
    main()
