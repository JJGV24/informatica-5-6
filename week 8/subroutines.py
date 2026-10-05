

def main():

    def calculate(a, b):
        answer = a + b
        print(f"{a} + {b} = {answer}")


    num1 = 10
    num2 = 15

    calculate(num1, num2)


    def average_value(a, b, c):
        average = (a + b + c)/3
        print(f"The average value is {round(average, 1)}")

    average_value(6,8,10)

    x = int(input("enter a number: "))
    y = int(input("enter another unmber: "))
    z = int(input("enter another unmber: "))

    average_value(x,y,z)

if __name__ == "__main__":
    main()

