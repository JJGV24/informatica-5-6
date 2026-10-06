

def main():

    def highest(a, b):
        if a < b:
            highest_num = b
            print(f"The highest number entered is {highest_num}")
        elif b < a:
            highest_num = a
            print(f"The highest number entered is {highest_num}")

    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    highest(num1, num2)




    def lowest(a, b, c):
        if a < b and a < c:
            lowest_num = a
            print(f"The lowest number entered is {lowest_num}")
        elif b < a and b < c:
            Lowest_num = b
            print(f"The lowest number entered is {lowest_num}")
        elif c < b and c < a:
            lowest_num = c
            print(f"The lowest number entered is {lowest_num}")


    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    num3 = int(input("enter another number: "))
    lowest(num1, num2, num3)










if __name__ == "__main__":
    main()

