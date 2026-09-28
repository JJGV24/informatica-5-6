

def main():

    not_validated = True

    while not_validated:
        try:
            num = int(input("Enter a number between 1 and 10: "))
            if num >= 1 and num <= 10:
                not_validated = False
        except ValueError:
            print("You must enter a number between 1 and 10.")

    not_validated2 = True

    while not_validated2:
        try:
            print("Enter a name:")
            name = input()
            print(f"Stored name: {name}")
        except ValueError:
            







if __name__ == "__main__":
    main()
