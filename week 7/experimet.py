def main():
    valid = []
    for i in range(1,11):
        valid.append(str(i))
    print("Welcome to hell")
    dang = True
    while dang:
        try:
            test = int(input("What table would you like to be tested on?: "))
            dang = False
        except ValueError:
            print("Invalid")
    abcd = True
    while abcd:
        try:
            max = int(input("Enter maximum value for the times table: "))
            abcd = False
        except ValueError:
            print("Invalid")
    max += 1

    for x in range(1,max):
        ans = x * int(test)
        oso = True

    while oso:
        try:
            answ = int(input(f"{x} times {test} is... "))
            oso = False
        except ValueError:
            print("Invalid ")
        if answ == ans:
            print("Correct! ")
        else:
            print("Incorrect ")



if __name__ == "__main__":
    main()
